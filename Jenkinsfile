pipeline {
    agent any
    parameters {
        booleanParam(name: 'Refresh',
                    defaultValue: false,
                    description: 'Read Jenkinsfile and exit.')
		    }
    stages {
        stage('Unit Tests') {
            steps {
                sh '''
                      python3 -m pytest /var/lib/jenkins/workspace/AppDeploy/prime/tests/test_unit.py
                   '''
            }
        }    
        stage('docker prune') {
            steps {
                sh 'sudo docker system prune -a -f'
            }
        }
        stage('docker compose') {
            steps {
                sh 'sudo docker-compose build'
            }
        }
        stage('git credentials') {
            steps {
                sh '''
                   git config --global user.email "ethanjohn99@gmail.com"
                   git config --global user.name "ethanjohn99"
                   git remote set-url origin git@github.com:ethanjohn99/PrimeAgeJenkins.git
                '''
            }
        }
        stage('feature_to_dev') {
            steps {
                sh '''
                    git checkout -f origin/dev
                    git merge origin/feature
                    git push origin HEAD:dev
                '''
            }
        }
        stage('dev_to_main'){
            steps {
                sh '''
                    git checkout origin/main
                    git merge origin/dev
                    git push origin HEAD:main
                '''
            }
        }
        stage('connect via ssh deploy server'){
            steps {
                sh '''
                   #!/bin/bash
                   ssh -i /home/jenkins/.ssh/mykey -o StrictHostKeyChecking=no ubuntu@18.132.39.166 << EOF
                   git checkout https://github.com/ethanjohn99/PrimeAgeJenkins.git
                   docker-compose -f /home/ubuntu/PrimeAgeJenkins/docker-compose.yaml down
                   docker system prune -a -f
                   docker-compose -f /home/ubuntu/PrimeAgeJenkins/docker-compose.yaml up -d
                   sudo rm -R /home/ubuntu/PrimeAgeJenkins
                   << EOF
                '''
            }
        }
        
    }
}
