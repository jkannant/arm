pipeline {
  agent { label 'windowns_node' }
  #tools {
        #jdk 'jdk1.7'
        #python 'python3.6'
    #}
  parameters {
    	string(name: 'repo_branch', defaultValue: 'master', description: 'The branch to be checked out')
	string(name: 'git_repo',  defaultValue: 'ssh://git@my-server.com/arm.git' description: 'Git repository from where we are going to checkout the code')
	}
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
    disableConcurrentBuilds()
    timeout(time: 10, unit: 'MINUTES')
	}
  triggers {
    pollSCM('* * * * *')
	}
  
  stages {
    
	stage('Checkout git repo') {
        steps {
            git branch: "${params.repo_branch}", url: "${params.git_repo}", credentialsId: 'git-credentials'
			}
		}
    stage('input1') {
		steps {
			bat 'ip_print input1.json'	
			}
		}
    stage('input2') {
		steps {
			bat 'ip_print input2.json'
			}
		}
	}
  post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'This will run only if successful'
        }
        failure {
            echo 'This will run only if failed'
        }
        unstable {
            echo 'This will run only if the run was marked as unstable'
        }
        changed {
            echo 'This will run only if the state of the Pipeline has changed'
            echo 'For example, if the Pipeline was previously failing but is now successful'
        }
    }
}
