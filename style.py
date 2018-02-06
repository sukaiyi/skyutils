BaseStyle = '''
QListWidget {
	color: gray;
	font-family: Droid Sans Mono,楷体;
	font-size: 10px;
	padding: 5px 0px 0px px;
	background: white;
	border-radius: 5px;
}
QListWidget::Item {
	padding-left: 10px;
	padding-right: 10px;
	padding-bottom: 5px;
}
ResultPanel {
	background: white;
}
'''

ResultLabelFailedStyle = '''
QLabel#messageLabel {
	border-radius: 5px;
	padding: 7px;
	color: red;
	background: #ffecb3;
	font-family: Consolas,楷体;
}
'''

ResultLabelSuccessStyle = '''
QLabel#messageLabel {
	border-radius: 5px;
	padding: 7px;
	color: black;
	background: #ffecb3;
	font-family: Consolas,楷体;
}
'''