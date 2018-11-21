##################################################--------Guilherme's Code--------###################################################################
#This function allows the user to download a file (it is the last command getting used, before this we have the upload function and a read function)#
#                                                                                                                                                   #
#                                                                                                                                                   #
#                                                                                                                                                   #
async def download(ma):                                                                                                                             #                                                                                                                                                   #
        if await logged(ma) == True:                                                                                                                 
###---------Getting user's id---------###############################################################################################################                                                                                                                      #                                                                                              #                                                                                                                                        #                              
            msg = 'Can you tell me the code of the file you want to download?'                                                                      #
            code = await getmsg(ma, msg) 
        
            if code == False:
                await timesup(ma)
                return
                                                                                                                                                    #            
            if await checkdbfiles('file_code', code) == True:                                                                                            #
                execution = "SELECT file_path FROM files WHERE file_code = ? AND discord_id = ?"
                filepath1 = c.execute(execution, [str(code), str(ma)])
                filepath2 = c.fetchone()[0]
                #filepath3 = str(filepath2).strip("'[(]),")                                                                                                       #                                                                                                                               #
         
                await client.send_file(ma, filepath2)                                                                                                    #
                msg = 'You can always download the file by right-clicking the file and using the discord option.'                                   #
                await sendmsg(ma, msg) 
                
                
                msg = 'Do you want to download another file? (y/n)'
                response = await getmsg(ma, msg)
                if response == False:
                    await timesup(ma)
                    return
                
                if response == 'Y' or response == 'y':
                    await download(ma)
                
                elif response.content == 'N' or response.content == 'n':
                    msg = 'I will see you next time!'
                    
                    await sendmsg(ma, msg)
                    return
                
                else:
                    msg = 'That is not a valid answer please try again with !download.'
                    
                    await sendmsg(ma, msg)
                    return
                    
                    
            else:                                                                                                                                   #
                msg = "The file you asked for doesn't seem to exist, recheck the file code and try again."                                          #
                await sendmsg(ma, msg)                                                                                                              #
                await download(ma)                                                                                                                  #
                                                                                                                                                    #
        else:                                                                                                                                       #
            msg = 'You are not logged in, please log in with !login before trying to download a file'                                               #
            await sendmsg(ma, msg)  
            return
#                                                                                                                                                   #
#                                                                                                                                                   #                                                                                                                                                              
#                                                                                                                                                   #                        
#                                                                                                                                                   #                                    
#                                                                                                                                                   #                                                
##########################--------This fucntion allows the user to read the files he has in his folder--------#######################################                                                                            
async def myfiles(ma):                                                                                                                              #
        if await logged(ma) == True:                                                                                                                      #
###---------Showing users their files---------####################################################################################################### 
            query = "SELECT file_name, file_code FROM files WHERE discord_id = ?"
            data = c.execute(query, [(str(ma))])                                                       #
            results = c.fetchall()                                                                                                                  #
                                                                                                                                                    #            
            for i in results:                                                                                                                       #
                msg = "File name: " + str(i[0]) + "   /   File code: " + str(i[1])                                                                            #
                                                                                                                                                    #             
                await sendmsg(ma, msg)                                                                                                              #
                                                                                                                                                    #            
                                                                                                                                                    #
        else:                                                                                                                                       #
            msg = 'You are not logged in, please log in with !login before trying to read your files'                                               #
            await sendmsg(ma, msg)                                                                                                                  #
#                                                                                                                                                   #
#                                                                                                                                                   #
#                                                                                                                                                   #
#                                                                                                                                                   #        
#                                                                                                                                                   #
#                                                                                                                                                   #
#                                                                                                                                                   #
#                                                                                                                                                   #
###############################################--------End of Guilherme's Code--------###############################################################                                                                                                                                                  #


