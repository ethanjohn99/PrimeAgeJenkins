pipeline {
    agent any
    parameters {
        booleanParam(name: 'Refresh',
                    defaultValue: false,
                    description: 'Read Jenkinsfile and exit.')
		    }
    stages {
         stage('Ansible Playbook') {
             steps {
                 sh 'ansible-playbook -v -i /var/lib/jenkins/workspace/AppTest/JenkinsAnsibleInstall/inventory.yaml /var/lib/jenkins/workspace/AppTest/JenkinsAnsibleInstall/playbook.yaml'
             }
         }
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
                   ssh -i /home/jenkins/.ssh/mykey -o StrictHostKeyChecking=no ubuntu@18.133.234.194 << EOF
                   docker-compose -f /home/ubuntu/AppTest/docker-compose.yaml down
                   docker system prune -a -f
                   docker-compose -f /home/ubuntu/AppTest/docker-compose.yaml up -d
                   sudo rm -R /home/ubuntu/App
                   << EOF
                '''
            }
        }
        
    }
}
