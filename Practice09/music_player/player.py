import pygame
import os

class MusicPlayer:
    def __init__(self, music_folder):
        self.music_folder = music_folder
        
        # Загружаем все треки
        self.playlist = [f for f in os.listdir(music_folder) if f.endswith(".wav") or f.endswith(".mp3")]
        self.playlist.sort()

        self.current_index = 0
        self.is_playing = False

        pygame.mixer.init()

    def load_track(self):
        if not self.playlist:
            return
        
        track_path = os.path.join(self.music_folder, self.playlist[self.current_index])
        pygame.mixer.music.load(track_path)

    def play(self):
        if not self.playlist:
            return
        
        self.load_track()
        pygame.mixer.music.play()
        self.is_playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False

    def next_track(self):
        if not self.playlist:
            return
        
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.play()

    def prev_track(self):
        if not self.playlist:
            return
        
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.play()

    def get_current_track_name(self):
        if not self.playlist:
            return "No tracks"
        return self.playlist[self.current_index]

    def get_position(self):
        # позиция в миллисекундах → переводим в секунды
        pos_ms = pygame.mixer.music.get_pos()
        if pos_ms == -1:
            return 0
        return pos_ms // 1000