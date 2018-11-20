#This function allows the user to download a file (it is the last command getting used, before this we have the upload function and a read function)
async def download(ma):
        
        if await logged(ma) == True:
            #Getting user's id
            msg = 'Can you tell me the code of the file you want to download?'
            code = await getmsg(ma, msg)
            
            if await checkdb('file_code', code) == True:
                execution = "SELECT file_path FROM files WHERE file_code = code AND discord_id = ?"
                filepath = c.execute(execution, [(str(ma))])
                file = open(filepath)
        
                await client.send_file(ma, file)
                msg = 'You can always download the file by right-clicking the file and using the discord option.' 
                await sendmsg(ma, msg)
                
                msg = 'Do you want to download another file? (y/n)'
                response = await getmsg(ma, msg)
                
                if response == 'Y' or response == 'y':
                    await download(ma)
                
                else:
                    continue

            
            else:
                msg = "The file you asked for doesn't seem to exist, recheck the file code and try again."
                await sendmsg(ma, msg)
                await download(ma)

        else:
            msg = 'You are not logged in, please log in with !login before trying to download a file'
            await sendmsg(ma, msg)
#
#            
#                        
#                                    
#                                                
#This fucntion allows the user to read the files he has in his folder                                                                            
async def myfiles(ma):
        if logged(ma) == True:
            #Showing user their files
            data = c.execute("SELECT file_name, file_code FROM users WHERE discord_id = ?")
            results = c.fetchall()
            
            for i in results:
                msg = "File name: " + i[3] + "   /   File code: " + i[2]
             
                await sendmsg(ma, msg)
            

        else:
            msg = 'You are not logged in, please log in with !login before trying to read your files'
            await sendmsg(ma, msg)    
#
#
#
#         
#
#
#
#
#


