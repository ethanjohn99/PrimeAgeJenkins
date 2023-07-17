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

        //stage('connect via ssh deploy server') {
        //    steps {
        //        sh '''
        //           #!/bin/bash
        //           ssh -i /home/jenkins/.ssh/myKey -o StrictHostKeyChecking=no ubuntu@172.31.33.237 << EOF
        //           ansible-playbook -v /home/ubuntu/playbook.yaml
        //           docker-compose -f /home/ubuntu/API2/docker-compose.yaml down
        //           docker system prune -a -f
        //           docker-compose -f /home/ubuntu/API2/docker-compose.yaml up -d
        //           sudo rm -R /home/ubuntu/API2
        //           << EOF
        //        '''
        //    }
        //}
        
    }
}
