from setuptools import setup, find_packages

setup(
    name='json_msg_logger',
    version='v0.0.1',
    author='Josias Nonato',
    author_email='josias.nonato1989@gmail.com',
    description='Lib para gerar logs no formato json com construção de mensagens ou uso de mensagens predefinidas. Compatível com grpc.',
    packages=find_packages(),
    install_requires=[
      "grpcio",
      "grpcio-tools",
    ],
)
