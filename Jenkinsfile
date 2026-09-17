pipeline {

    agent any

    stages {

        stage('Pytest') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install -r requirements.txt
                pytest -v
                '''
            }
        }

        stage('Build') {
            steps {
                sh '''
                docker build -t banking-app:v1 .
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop banking-app || true
                docker rm banking-app || true

                docker run -d \
                --name banking-app \
                -p 7030:7030 \
                banking-app:v1
                '''
            }
        }
    }
}
