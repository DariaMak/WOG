pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t wogapp .'
            }
        }

        stage('Run') {
            steps {
                sh 'docker run -d -p 8777:80 --name=wogapp_container -v $(pwd)/Scores.txt:/Scores.txt wogapp'
            }
        }

        stage('Test') {
            steps {
                sh 'python tests/e2e.py'
            }
        }

        stage('Finalize') {
            steps {
                sh 'docker stop wogapp_container'
                sh 'docker rm wogapp_container'
                withCredentials([usernamePassword(credentialsId: 'dockerHubCredentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'docker login -u $DOCKER_USER -p $DOCKER_PASS'
                    sh 'docker push myapp'
                }
            }
        }
    }
}