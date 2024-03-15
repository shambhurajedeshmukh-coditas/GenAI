from setuptools import find_packages,setup
setup(
    name='mcqgenerator',
    version='0.0.1',
    author="Shambhuraje Deshmukh",
    author_email="shambhurd9@gmail.com",
    install_requirement=["OpenAI","langchain","Streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)