pipeline {
    agent any

    environment {
        // The branch name is usually provided by Jenkins in multibranch pipelines.
        // This can differ if you're using a different job type.
        BRANCH_NAME = "${env.BRANCH_NAME}"
    }

    stages {
        stage('Install Dependencies') {
            steps {
                // Activate Anaconda and install dependencies
                bat 'call C:\\Users\\zaema\\anaconda3\\Scripts\\activate.bat && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Ensure the right Anaconda environment is activated before running tests
                bat 'call C:\\Users\\zaema\\anaconda3\\Scripts\\activate.bat && pytest'
            }
        }

        stage('Deploy') {
            steps {
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
