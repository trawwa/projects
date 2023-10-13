pipeline {
    agent any
    parameters {
        string(name: 'promt', defaultValue: '', description: 'Здесь нужно ввести запрос к GPT.')
    }
    stages {
        // stage("Загрузка скрипта") {
        //     steps {
        //         script {
        //             // def gpt2 
        //             // fileLoader.withGit('https://github.com/trawwa/projects.git', 'main', null, '') {
        //             //     gpt2 = load('pyprojects/gpt/gpt2.py');
        //             }  
        //         }
        //     }
        
        stage("Установка зависимостей") {
            steps {
                script{
                    sh "pip3 install -r requirements.txt"
                }
            }
        }
        stage("Выполнение скрипта") {
            steps {
                script {
                    sh "python3 ./pyprojects/gpt/gpt2.py ${promt}"
                    //gpt2.main()
                }
            }
        }
    }
}
    post {
        always {
            cleanWs()
        }
    }
