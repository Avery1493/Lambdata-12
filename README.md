# Lambdata-12

https://test.pypi.org/project/avery1493-Lambdata-12/2.0/
pip install -i https://test.pypi.org/simple/ avery1493-Lambdata-12==1.0

python setup.py sdist bdist_wheel
twine upload --repository-url https://test.pypi.org/legacy/ dist/*