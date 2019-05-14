import os

from dotenv.main import DotEnv


def load_env():
    env_path = os.environ.get('ENV_PATH', './.env')
    print(f"* Env Path: {env_path}")

    dotenv = DotEnv(env_path, verbose=False)
    dotenv_dict = dotenv.dict()
    print("* Loaded .env")
    for k, v in dotenv_dict.items():
        print(f'** {k}={v}')
    dotenv.set_as_environment_variables(override=True)
