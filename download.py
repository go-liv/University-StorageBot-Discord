#This function allows the user to download a file (it is the last command getting used, before this we have the upload function and a read function)
async def download(ma):
        
        if logged(ma) == True:
            #Getting user's id
            selection = ("SELECT id FROM users WHERE discord_id = ?")
            userid = c.execute(selection,[(str(ma))])
            
            msg = 'Can you tell me the code of the file you want to download?'
            code = await getmsg(ma, msg)
            
            if await checkdb('file_code', code) == True:
                file = c.execute("SELECT file_path FROM files WHERE file_code = code AND user_id = userid")
                file = open(file)
        
                await client.send_file(ma, file)
                msg = 'You can always download the file by right-clicking the file and using the discord option.' 
                await sendmsg(ma, msg)
                
                
                
                
                
                #####ask user if wants to download another file and make code for that etc...
            
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
            data = c.execute("SELECT file_name, file_code FROM files WHERE user_id = ?")
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


