# Task 1: software configuration.

### Subtask 1: Why did I choose to participate in the Dare IT Challenge?

Hello, World :) Despite I'm already working as manual QA, this is my first experience in automation testing. Whats driving me? I'm interesting to improve my QA knowledge  ~~and automate boring regression tests~~ to feel more confident in speedly mooving QA sphere. Hope to learn new usefull things for myself and apply them on work  


# Task 2: selectors.

### Header element:
 - //*[text()='Scouts Panel']
 - /html/body/div/form/div/div[1]/h5
 - //*[@id="__next"]//child::h5

### Labels:
Login: 
 - /html/body/div/form/div/div[1]/div[1]/label
 - //*[@id="login-label"]
 - //*[text()='Login']

Password:
 - /html/body/div/form/div/div[1]/div[2]/label
 - //*[@id='password-label']
 - //*[text()='Password']

### Login field:
 - /html/body/div/form/div/div[1]/div[1]/div/input
 - //*[@id='login']
 - //input[starts-with(@name, 'login')]

### Password field:
 - /html/body/div/form/div/div[1]/div[2]/div/input
 -  //*[@id='password']
 - //input[starts-with(@name, 'password')]

### Remind password: 
 - /html/body/div/form/div/div[1]/a
 - //*[text()='Remind password']
 - //child::div/a

### Language selert dropdown: 
 - /html/body/div/form/div/div[2]/div/div
 - //*[starts-with(@class, 'MuiSelect-root')]
 - //div[contains(@aria-haspopup, 'listbox')]
 - English: //input[@value='en']
 - Polish: //input[@value='pl']

### Sign-in button:
 - /html/body/div/form/div/div[2]/button/span[2]
 - //button/span[2]
 - //span[text()='Sign in']
