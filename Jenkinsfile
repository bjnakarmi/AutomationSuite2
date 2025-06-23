pipeline{
	agent any
	stages{
		stage('Checkout Code'){
			steps{
				git branch : 'main',
				url : 'https://github.com/bjnakarmi/AutomationSuite2.git'
			}
		}
		stage('Install Dependencies'){
			steps{
				bat 'pip install -r requirements.txt'
			}
		}
		stage('tests'){
			steps{
				bat 'pytest tests/ --html=report.html'
			}
		}
		stage('Archive Artifacts'){
			steps{
				archiveArtifacts artifacts : 'report.html'
			}
		}
	}

}