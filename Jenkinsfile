pipeline {
    agent { label 'node1' }

    stages {

        stage('Checkout') {
            steps {
                echo "Code Checked Out Successfully"
            }
        }

        stage('Build') {
            steps {
                sh '''
                echo "Building Application..."
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                echo "Testing Application..."
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                echo "Deploying Application..."
                '''
            }
        }
    }

    post {
        always {
            echo "Pipeline completed successfully"
        }
    }
}
