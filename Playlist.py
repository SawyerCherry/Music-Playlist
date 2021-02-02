from Song import Song

class Playlist:
  def __init__(self):
    self.__first_song = None


  # TODO: Create a method called add_song that creates a Song object and adds it to the playlist. This method has one parameter called title.

  def add_song(self, title):
    current_song = self.__first_song
    new_song = Song(title)

    if current_song == None:
      self.__first_song = new_song
    else: 
      while current_song.get_next_song() != None:
        current_song = current_song.get_next_song()
      current_song.set_next_song(new_song)
    



  # TODO: Create a method called find_song that searches for whether a song exits in the playlist and returns its index. The method has one parameters, title, which is the title of the song to be searched for. If the song is found, return its index.

  def find_song(self, title):
    current_song = self.__first_song
    exists = False
    index = 0

    while current_song != None and not exists:
      if current_song.get_title() == title:
        exists = True
      else:
        current_song = current_song.get_next_song()
        index + 1
    return index
    


  # TODO: Create a method called remove_song that removes a song from the playlist. This method takes one parameter, title, which is the song that should be removed. 

  def remove_song(self, title):
    pass



  # TODO: Create a method called length, which returns the number of songs in the playlist.

  def length(self):
    pass


  # TODO: Create a method called print_songs that prints a numbered list of the songs in the playlist.

  # Example:
  # 1. Song Title 1
  # 2. Song Title 2
  # 3. Song Title 3

  def print_songs(self):
    pass

  