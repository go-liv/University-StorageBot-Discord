'''
##################################################--------Guilherme's Code--------###################################################################
#--------------------------------------------------------Download Function--------------------------------------------------------------------------#
#This function allows the user to download a file (it is the last command getting used, before this we have the upload function and a read function)#
#You can call the function by simply passing the author of the message, in this case it is the variable ma(message.author)                          #                                                                                                                         #
#The functionality of the function is to ask the user for a code, which is assigned to his file when uploaded, and then search for this code in the #                                                                                                                                                   #
#database. When the code is found, the function grabs the file path in the same row as the code and sends the file from that file path to the user  #
#as a message                                                                                                                                       #
#####################################################################################################################################################
'''                 
async def download(ma):                                                                                                                             #                                                                                                                                                   #
        if databaseCheck(ma).logged() == True:                                                                                                      #           
###---------Getting user's id---------###############################################################################################################                                                                                                                      #                                                                                              #                                                                                                                                        #                              
            msg = 'Can you tell me the code of the file you want to download?'                                                                      #
            code = await getmsg(ma, msg, False)                                                                                                     #
                                                                                                                                                    #
            if code == False:                                                                                                                       #
                await timesup(ma)                                                                                                                   #
                return                                                                                                                              #
                                                                                                                                                    #            
            if await checkdbfiles('file_code', code) == True:                                                                                       #
                execution = "SELECT file_path FROM files WHERE file_code = ? AND user = ?"                                                          #
                filepath1 = c.execute(execution, [str(code), str(ma)])                                                                              #
                filepath2 = c.fetchone()[0]                                                                                                         #                                                                                                                             #
                                                                                                                                                    #
                await client.send_file(ma, filepath2)                                                                                               #
                msg = 'You can always download the file by right-clicking the file and using the discord option.'                                   #
                await sendmsg(ma, msg)                                                                                                              #
                                                                                                                                                    #
                                                                                                                                                    #
                msg = 'Do you want to download another file? (y/n)'                                                                                 #
                response = await getmsg(ma, msg, False)                                                                                             #
                if response == False:                                                                                                               #
                    await timesup(ma)                                                                                                               #
                    return                                                                                                                          #
                                                                                                                                                    #
                if response == 'Y' or response == 'y':                                                                                              #
                    await download(ma)                                                                                                              #
                                                                                                                                                    #
                elif response == 'N' or response == 'n':                                                                                            #
                    msg = 'I will see you next time!'                                                                                               #
                                                                                                                                                    #
                    await sendmsg(ma, msg)                                                                                                          #
                    return                                                                                                                          #
                                                                                                                                                    #
                else:                                                                                                                               #
                    msg = 'That is not a valid answer please try again with !download.'                                                             #
                                                                                                                                                    #
                    await sendmsg(ma, msg)                                                                                                          #
                    return                                                                                                                          #
                                                                                                                                                    #
                                                                                                                                                    #
            else:                                                                                                                                   #
                msg = "The file you asked for doesn't seem to exist, recheck the file code and try again."                                          #
                await sendmsg(ma, msg)                                                                                                              #
                await download(ma)                                                                                                                  #
                                                                                                                                                    #
        else:                                                                                                                                       #
            msg = 'You are not logged in, please log in with !login before trying to download a file'                                               #
            await sendmsg(ma, msg)                                                                                                                  #
            return                                                                                                                                  #
#                                                                                                                                                   #
#                                                                                                                                                   #                                                                                                                                                              
#                                                                                                                                                   #                        
#####################################################################################################################################################                                                                                                                                                   #                                    
'''                                                                                                                                                                                                 
#----------------------------------------------------------My Files Function------------------------------------------------------------------------#                                                                            
#This function was made in order to show the users the files they have stored in our storage bot                                                    #
#It can be called like the download function just by passing the user's ma                                                                          #
#In quick terms, the function searches the database for the files and shows the user the file name and the respective assigned code, all this is    #
#made by searching the database for the row where the user's ma is.                                                                                 #
#####################################################################################################################################################
'''
async def myfiles(ma):                                                                                                                              #
        if databaseCheck(ma).logged() == True:                                                                                                      #
###---------Showing users their files---------####################################################################################################### 
            query = "SELECT file_name, file_code FROM files WHERE user = ?"                                                                         #
            data = c.execute(query, [(str(ma))])                                                                                                    #
            results = c.fetchall()                                                                                                                  #
                                                                                                                                                    #            
            for i in results:                                                                                                                       #
                msg = "File name: " + str(i[0]) + "   /   File code: " + str(i[1])                                                                  #
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
#
'''                                                                                                                                                   #
###############################################--------End of Guilherme's Code--------###############################################################                                                                                                                                                  #
'''
