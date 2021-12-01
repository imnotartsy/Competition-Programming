# Every month, there are millions of streamers who stream in a variety of different categories. For this challenge, you’ll be working on writing a data structure that will be storing the name of streamers streaming, the number of views they currently have, as well as the category they are streaming in.
# The initial input of streamer information will come as a list of strings:

# Example: [Ninja, 100000, Fortnite, Pokimane, 40000, Valorant]
# This is interpreted as Ninja has 100,000 views and is streaming Fortnite, and Pokimane has 40000 views and is streaming Valorant. The names of the streamers will be unique. You will not be given any negative numbers for view counts.
# You will also be given a list of commands, that will manipulate the streamer data or require output:
# (All Examples are based on the original input above)


# StreamerOnline - Add a new streamer to the data structure. The name will be unique. 
#     Example Input: StreamerOnline, AOC, 75000, Just Chatting -> [Ninja, 100000, Fortnite, Pokimane, 40000, Valorant, AOC, 75000, Just Chatting ]

# UpdateViews - Update the views of a streamer name, who is streaming in the respective category, to the provided number of views.
#     Example Input: UpdateViews, Ninja, 120000, Fortnite -> Update Ninjas viewer count to 120,000 If the streamer is not streaming within that category, this command can be ignored.

# UpdateCategory - Update the category of a streamer name, who is streaming in the respective category, to the provided category.
#     Example Input: UpdateCategory, Ninja, Fortnite, Warzone -> Update Ninjas category to Warzone If the streamer is not streaming within that category, this command can be ignored.

# StreamerOffline - Remove the streamer from the data structure, if they are streaming within the given category
#     Example Input: StreamerOffline, Ninja, Fortnite -> [Pokimane, 40000, Valorant] only this data will exist within the data structure. If the streamer is not streaming within that category, this command can be ignored.

# ViewsInCategory - Returns the amount of viewers watching a certain category. Returns 0 if category does not exist.
#     Example Input: ViewsInCategory, Fortnite -> 100000 as Ninja is the only streamer within the category

# TopStreamerInCategory - Returns the streamer with the highest view count in a certain category. Returns null if the category does not exist or there is nobody currently streaming in the category.
#     Example Input: TopStreamerInCategory, Valorant -> Pokimane as Pokimane is the only streamer within the category

# TopStreamer - Returns the streamer with the highest view count currently streaming. Returns null if there is nobody currently streaming.
#     Example Inputs: TopStreamer -> Ninja as Ninja has the highest view count.


# These commands will be strung together, for example:
# StreamerOnline, Bugha, 75000, Fortnite, StreamerOnline, Tenzo, 30000, Valorant, ViewsInCategory, Fortnite, TopStreamerInCategory, Valorant
# Expected Return: [175000, Pokimane]
# Notes: There will never be a tie in view counts There will never be duplicate category or streamer Names. Find an error or bug? Let us know at University@twitch.tv

def solution(streamerInformation, commands):
    
    ret = []
    
    command_idx = 0
    
    ## Handle 'switch statement' for command
    while command_idx < len(commands):
        curr_command = commands[command_idx]
        print(curr_command, "has been selected")
        
        
        ## Top Streamer
        if curr_command == "TopStreamer":
            # Returns the streamer with the highest view count currently streaming.
            # Returns null if there is nobody currently streaming.
            # Example Inputs: TopStreamer -> Ninja as Ninja has the highest view count.
            if len(streamerInformation) == 0:
                return None
            top_idx = 0
            for streamer in range(len(streamerInformation)):
                # print("Checking streamer:", streamerInformation[streamer])

                if isinstance(streamerInformation[streamer], int):
                    if streamerInformation[streamer] > streamerInformation[top_idx+1]:
                        top_idx = streamer-1
            ret.append(streamerInformation[top_idx])


        ## StreamerOnline
        elif curr_command == "StreamerOnline":
            # Add a new streamer to the data structure. The name will be unique.
            # Example Input: StreamerOnline, AOC, 75000, Just Chatting -> [Ninja,
            # 100000, Fortnite, Pokimane, 40000, Valorant, AOC, 75000, Just Chatting ]
            streamerInformation.append(commands[command_idx+1])
            streamerInformation.append(commands[command_idx+2])
            streamerInformation.append(commands[command_idx+3])
            print("Added", commands[command_idx+1], commands[command_idx+2], commands[command_idx+1])
            command_idx += 3
            
            print("New datastructure:", streamerInformation)
            
            
        ## UpdateViews
        elif curr_command == "UpdateViews":
            # Update the views of a streamer name, who is streaming in the respective
            # category, to the provided number of views.
            # Example Input: UpdateViews,
            # Ninja, 120000, Fortnite -> Update Ninjas viewer count to 120,000 If the
            # streamer is not streaming within that category, this command can be
            # ignored.
            for streamer in range(int(len(streamerInformation)/3)):
                print("Checking streamer:", streamerInformation[streamer*3])

                if streamerInformation[streamer*3] == commands[command_idx+1]:
                    streamerInformation[streamer*3+1] = commands[command_idx+2]
                    command_idx += 2
                    print("New datastructure", streamerInformation)
            
            
        ## UpdateCategory
        elif curr_command == "UpdateCategory":
            # Update the category of a streamer name, who is streaming in the
            # respective category, to the provided category.
            # Example Input: UpdateCategory, Ninja, Fortnite, Warzone -> Update Ninjas
            # category to Warzone If the streamer is not streaming within that
            # category, this command can be ignored.
            for streamer in range(int(len(streamerInformation)/3)):
                print("Checking streamer:", streamerInformation[streamer*3])

                if streamerInformation[streamer*3] == commands[command_idx+1] and streamerInformation[streamer*3+2] == commands[command_idx+2]:
                    streamerInformation[streamer*3+2] = commands[command_idx+3]
                    command_idx += 2
                print("New datastructure", streamerInformation)


        ## ViewsInCategory
        elif curr_command == "ViewsInCategory":
            # Returns the amount of viewers watching a certain category.
            # Returns 0 if category does not exist.
            # Example Input: ViewsInCategory, Fortnite -> 100000 as Ninja is the only
            # streamer within the category

            if len(streamerInformation) == 0:
                return 0
            
            sum_views = 0
            for streamer in range(int(len(streamerInformation)/3)):
                print("Checking streamer:", streamerInformation[streamer*3])

                if streamerInformation[streamer*3+2] == commands[command_idx+1]:
                    print(streamerInformation[streamer*3], "is in", commands[command_idx+1])
                    sum_views += int(streamerInformation[streamer*3+1])
            ret.append(str(sum_views))
            
            
        ## TopStreamerInCategory
        elif curr_command == "TopStreamerInCategory":
            # Returns the amount of viewers watching a certain category.
            # Returns 0 if category does not exist.
            # Example Input: ViewsInCategory, Fortnite -> 100000 as Ninja is the only
            # streamer within the category

            top_streamer = 0
            if len(streamerInformation) == 0:
                return 0
            for streamer in range(int(len(streamerInformation)/3)):
                print("Checking streamer:", streamerInformation[streamer*3])

                if streamerInformation[streamer*3+2] == commands[command_idx+1]:
                    top_streamer = streamer*3
            
            ret.append(streamerInformation[top_streamer]) 
            
        
        ## StreamerOffline
        elif curr_command == "StreamerOffline":
            # Remove the streamer from the data structure, if they are streaming
            # within the given category
            # Example Input: StreamerOffline, Ninja,Fortnite -> [Pokimane, 40000,
            # Valorant] only this data will exist within the data structure. If
            # the streamer is not streaming within that category, this command can
            # be ignored.

            if len(streamerInformation) == 0:
                return 0
            
            streamer = 0
            while streamer < int(len(streamerInformation)/3):
                print("Checking streamer:", streamerInformation[streamer*3])

                if streamerInformation[streamer*3] == commands[command_idx+1] and streamerInformation[streamer*3+2] == commands[command_idx+2]:
                    streamerInformation[streamer*3+2] = commands[command_idx+2]
                    command_idx += 2
                    del streamerInformation[streamer*3]
                    del streamerInformation[streamer*3]
                    del streamerInformation[streamer*3]
                
                streamer += 1
                print("New datastructure", streamerInformation)
                

            
        # Next Command
        command_idx += 1


    return ret
