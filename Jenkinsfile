pipeline {
    agent any

    stages {
        stage('Initialize') {
            steps {
                script {
                    // Extract the branch name from the GIT_BRANCH environment variable
                    env.BRANCH_NAME = env.GIT_BRANCH.split('/')[-1]
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'call C:\\Users\\zaema\\anaconda3\\Scripts\\activate.bat && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'call C:\\Users\\zaema\\anaconda3\\Scripts\\activate.bat && pytest .'
            }
        }

        stage('Deploy') {
            steps {
                script {
                    if (env.BRANCH_NAME == 'master') {
                        echo "Deploying to production as branch is ${env.BRANCH_NAME}..."
                        // Insert your deployment commands here
                    } else {
                        echo "Skipping deployment as branch is ${env.BRANCH_NAME}."
                    }
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline execution complete on branch ${env.BRANCH_NAME}!"
        }
    }
}
