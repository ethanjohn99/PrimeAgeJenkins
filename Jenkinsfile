pipeline {
    agent any
    parameters {
        booleanParam(name: 'Refresh',
                    defaultValue: false,
                    description: 'Read Jenkinsfile and exit.')
		    }
    stages {
        // stage('Pre') { hello push
        //     steps {
        //         sh 'ansible-playbook -v -i /home/jenkins/.jenkins/workspace/FlaskApp/inventory.yaml /home/jenkins/.jenkins/workspace/FlaskApp/playbook.yaml'
        //     }
        // }
        // stage('Test') { 
        //     steps {
        //         sh 'sudo pytest /home/jenkins/.jenkins/workspace/FlaskApp/'
        //     }
        // }
        stage('Unit Tests') {
            steps {
                sh '''
                      python3 -m pytest /var/lib/jenkins/workspace/AppTest/prime/tests/test_unit.py
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

        stage('connect via ssh deploy server') {
            steps {
                sh '''
                   #!/bin/bash
                   ssh -i /home/jenkins/.ssh/mykey -o StrictHostKeyChecking=no ubuntu@13.41.76.113 << EOF
                   docker-compose -f /home/ubuntu/App/docker-compose.yaml down
                   docker system prune -a -f
                   docker-compose -f /home/ubuntu/App/docker-compose.yaml up -d
                   sudo rm -R /home/ubuntu/App
                   << EOF
                '''
            }
        }
        
    }
}
