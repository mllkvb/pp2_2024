import pygame
import sys

pygame.init()

sc=pygame.display.set_mode((800, 600))
pygame.display.set_caption("Spotify")


pygame.mixer.init()
playlist = ["Кайф Ты Поймала.mp3","Bruno Mars - Grenade.mp3","Eminem feat Rihanna - Love the way u lie (AV mix version).mp3","Gerry & The Pacemakers - You ll Never Walk Alone.mp3","SHINee__Stand_B.mp3","true.moi.demon.mp3"]
current_track_index = 0
pygame.mixer.music.load(playlist[current_track_index])
music = pygame.mixer.music.load("Кайф Ты Поймала.mp3")
play = False
pause = False
pos = 0 # start from stopped moment;

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not play:
                    pygame.mixer.music.play(start=pos)
                    play = True
                    pause = False
                elif not pause:
                    pygame.mixer.music.pause()
                    pos = pygame.mixer.music.get_pos()/1000 # allows you to get the current music playback position in seconds instead of milliseconds.
                    pause = True
                else:
                    pygame.mixer.music.unpause()
                    play = True
                    pause = False
            elif event.key == pygame.K_RIGHT:
                current_track_index = (current_track_index + 1) % len(playlist) # Это позволяет циклически переключаться между треками в плейлисте.
                pygame.mixer.music.load(playlist[current_track_index]) # Загружает следующий трек из плейлиста в музыкальный модуль Pygame.
                pygame.mixer.music.play() # Начинает воспроизведение загруженного трека.
            elif event.key == pygame.K_LEFT:
                current_track_index=(current_track_index-1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track_index]) # Загружает предыдущий трек из плейлиста в музыкальный модуль Pygame.
                pygame.mixer.music.play() # Начинает воспроизведение загруженного трека.
            
        sc.fill((30, 215, 96))

        font=pygame.font.Font(None, 36) # Создается объект шрифта с размером 36. 
        text=font.render("Oinap jatyr:"+ playlist[current_track_index], True, (0, 0, 0)) # Здесь создается изображение текста для отображения на экране. 
        sc.blit(text, (50, 50)) # С помощью этой строки изображение текста (text) рисуется на экране в позиции (50, 50).

        font_plist=pygame.font.Font(None, 30) # playlist font.
        for i, song in enumerate(playlist): # перебирает все треки в плейлисте
            color = (255, 0, 0) if i == current_track_index else (0, 0, 0)
            playlist_text = font_plist.render(str(i + 1) + '.'+ song, True, color)
            sc.blit(playlist_text, (70, 170 + i * 30))

        pygame.display.update()
    pygame.time.wait(10)