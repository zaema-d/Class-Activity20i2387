pipeline {
    agent any

    environment {
        // This is now set using the GIT_BRANCH environment variable
        BRANCH_NAME = "${env.GIT_BRANCH.split('/')[-1]}"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Deploy') {
            steps {
                // Here we're using the BRANCH_NAME environment variable
                script {
                    if (BRANCH_NAME == 'master') {
                        echo "Deploying to production as branch is ${BRANCH_NAME}..."
                        // Insert your deployment commands here
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
