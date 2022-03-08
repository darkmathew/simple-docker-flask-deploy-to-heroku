import click
from simple_df_deploy import create_docker_file, create_steps_file


@click.command()
@click.option('--image_name', '-img', default='YOUR_IMAGE_NAME', help="Type the name of the image you want to give the image to be created.")
@click.option('--heroku_app_name', '-hap', default='YOUR_DESIRED_HEROKU_APP_NAME', help="Type the name of the heroku app you want to give the app to be created.")
@click.option('--run', '-r', default='app', help="Type the name of the file that runs your flask application.")
def cli(image_name, heroku_app_name, run):
    create_docker_file(run)
    create_steps_file(run, image_name, heroku_app_name)
    print('Files Created')


if __name__ == '__main__':
    cli()