pipeline {
    agent any
    parameters {
        string(name: 'promt', defaultValue: '', description: 'Здесь нужно ввести запрос к GPT.')
    }
    stages {
        stage("Загрузка скрипта") {
            steps {
                def gpt2 
                fileLoader.withGit('https://github.com/trawwa/projects.git', 'main', null, '') {
                    gpt2 = fileLoader.load('pyprojects/gpt/gpt2.py');
                }
            }
        }
        stage("Установка зависимостей") {
            sh "pip install -r requirements.txt"
        }
        stage("Выполнение скрипта") {
            steps {
                gpt2.main()
            }
        }
    }
}