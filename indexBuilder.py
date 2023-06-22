import pandas

htmlFile = open('index.html','w', newline='')
csvFile = pandas.read_csv("output.csv")
csvFile = csvFile.groupby('repository')['data'].apply(list).reset_index(name='data')
templateFile = open('template.html','r')

for line in templateFile:
    htmlFile.write(line)

for ind in csvFile.index:
    htmlFile.write(f'''   <tr>
          <td>{csvFile['repository'][ind]}</td>
          ''')
    buttonString = ''
    for userString in csvFile['data'][ind]:
        users = [x.strip() for x in userString.replace('"',"").replace('[',"").replace(']',"").replace('\'',"").split(',')]
        if(users[3] == 'admin'):
           role = 'adminUser'     
        else:
            role = 'maintainUser'
        buttonString += f'''
        <button class="{role}" onclick="copyToClipboard('{users[1]}')">
            {users[1]} 
            <img src="data/adminCopyLogo.svg" />
        </button>
        '''
    htmlFile.write(f'''
      <td>
        {buttonString}
      </td>
    </tr>
    ''')    
    
htmlFile.write('''
  </tbody>
    </table>
    <footer>
      <div id="footerDiv">
        <a href="https://infoblox.atlassian.net/secure/CreateIssue.jspa?pid=10019">missing info</a>
        <br>
        <p>
          Maintained by team DEVOPS SRE.
        </p>
      </div>
    </footer>
  </body>
</html>''')

htmlFile.close()
templateFile.close()
