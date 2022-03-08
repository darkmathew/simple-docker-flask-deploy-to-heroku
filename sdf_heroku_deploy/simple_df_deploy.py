import platform
from os import remove
from os.path import isfile


def get_docker_image_type():
    while True:
        
        version = input("""[*] Choose a Python Docker Image version [*]\n(1) - aplpine\n(2) - buster\n(3) - bullseye\nType here: """)
        
        try:
            version = int(version)
        except:
            print('<ERROR> Type a integer value')
            continue

        if version not in range(1, 4):
            print('<ERROR> Version needs to be in range (1, 3)')
            continue
        
        option_values = {
            1: "aplpine",
            2: "buster",
            3: "bullseye"
        }
        return option_values[version]


def get_local_python_version():
    python_version = platform.python_version()[:4]
    return python_version


def create_docker_file(run):
    file = 'Dockerfile'
    remove_file(file)

    content = get_docker_content(run)

    with open('Dockerfile', mode='w') as w:
        w.write(content)


def get_run_script_file():
    run = input('[Main Script] Enter the name of the file that runs your flask application: ')
    if '.py' in run:
        run = run.replace(".py", "")
    return run
    

def remove_file(file):
    if isfile(file):
        remove(file)


def get_docker_content(run):
    content = ''
    
    image_type = get_docker_image_type()
    py_version = get_local_python_version()
    
    content += f'FROM python:{py_version}-{image_type}\n\n'
    content += 'RUN pip install --upgrade pip\n\n'
    content += 'RUN mkdir /app\n\n'
    content += 'WORKDIR /app\n\n'
    content += 'ADD . .\n\n'
    content += 'RUN pip install -r requirements.txt\n\n'
    content += f'CMD gunicorn {run}:app --bind 0.0.0.0:$PORT --reload\n\n'

    return content


def create_steps_file(run, image_name, heroku_app_name):
    file = 'steps.txt'
    remove_file(file)

    content = ""
    content += f"""[1] - In your {run}.py file add the line:\nif __name__ == '__main__':\n     app.run(host='0.0.0.0')\n\n"""
    content += f"[2] - Run the command in terminal: docker build -t {image_name}:latest .\n\n"
    content += f"[3] - Wait for the operation to finish\n\n"
    content += f"[4] - Run the command in terminal: docker run -d -p 5000:5000 {image_name}\n\n"
    content += f"[5] - Check if your application is running on http://localhost:5000\n\n"
    content += f"[6] - If everything is ok, proceed to the next steps.\n\n"
    content += f"[7] - Run the command in terminal: heroku create {heroku_app_name}\n\n"
    content += f"[8] - Run the command in terminal: heroku container:login\n\n"
    content += f"[9] - If the login was successful, proceed to the next steps.\n\n"
    content += f"[10] - Run the command in terminal: heroku container:push web --app {heroku_app_name}\n\n"
    content += f"[11] - Run the command in terminal: heroku container:release web --app {heroku_app_name}\n\n"
    content += f"[12] - Visit your web app >> https://{heroku_app_name}.herokuapp.com\n\n"

    with open(file, encoding='utf-8', mode='w') as w:
        w.write(content)

def main():
    run = get_run_script_file()
    image_name = input('Enter the name of the image you want to give the image to be created: ')
    if image_name == "":
        image_name = "YOUR_IMAGE_NAME"

    heroku_app_name = input('Enter the name of the heroku app you want to give the app to be created: ')
    if heroku_app_name == "":
        heroku_app_name = "YOUR_DESIRED_HEROKU_APP_NAME"

    create_docker_file(run)
    create_steps_file(run, image_name, heroku_app_name)


if __name__ == '__main__':
    main()