pipeline {
    agent any

    environment {
        BRANCH_NAME = '' // Initialize an env var 
    }

    stages {
        stage('Prepare') {
            steps {
                script {
                    // Extract the branch name and store it in the variable
                    BRANCH_NAME = sh(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies from requirements.txt
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run pytest
                    sh 'pytest'
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    
                    if (BRANCH_NAME == 'master') {
                        echo "Deploying to production as branch is ${BRANCH_NAME}..."
                        
                    } else {
                        echo "Skipping deployment as branch is ${BRANCH_NAME}."
                        
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline execution complete on branch ${BRANCH_NAME}!"
        }
    }
}
