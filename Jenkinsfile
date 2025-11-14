pipeline {
    agent { label 'node1' }

    environment {
        DOCKERHUB_USER = "awinash8"   // Your DockerHub username
        IMAGE = "jenkins-demo"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "Pulling latest code..."
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image..."
                    sh """
                    docker build -t ${DOCKERHUB_USER}/${IMAGE}:latest .
                    """
                }
            }
        }

        stage('Login to DockerHub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh """
                    echo "$PASS" | docker login -u "$USER" --password-stdin
                    """
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    echo "Pushing Docker image..."
                    sh """
                    docker push ${DOCKERHUB_USER}/${IMAGE}:latest
                    """
                }
            }
        }

        stage('Done') {
            steps {
                echo "Docker Build and Push Complete!"
            }
        }
    }
}
