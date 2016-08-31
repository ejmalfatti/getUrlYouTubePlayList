Obtener la lista de URL de un playlists de YouTube
-

Escribí un sencillo script en **Python** que obtiene cada URL individual de cada video que compone una lista de reproducción de YouTube.
Por ejemplo de la siguiente captura de pantalla:
![](https://ejmalfatti.github.io/imagenes//playlist.png) 

En ese Playlists hay 40 videos, y el script obtiene cada url y las guarda en un archivo de texto en el mismo directorio desde donde se ejecuta el script.

La URL que hay que utilizar es del playlists: https://www.youtube.com/playlist?list=PLU8oAlHdN5Bkn-KS1sRFlSEnXXcAtAJ9P

El script se ejecutaria de la siguiente manera:

	$ python getUrlYouTubePlayList.py https://www.youtube.com/playlist?list=PLU8oAlHdN5Bkn-KS1sRFlSEnXXcAtAJ9P

Va generar un archivo de texto llamado "**playlists.txt**"

![](https://ejmalfatti.github.io/imagenes/script.png) 

En este caso hace un **print ** para que se pueda apreciar lo que hace este simple script, solo eso hace.

El resultado seria este:

![](https://ejmalfatti.github.io/imagenes/lista.png) 

Se ejecuta el script y luego se lee con un "cat " el archivo que crea el script y al final, de cortesia dice cuantos videos tiene dicho playlists.

![](https://ejmalfatti.github.io/imagenes/videos.png)

Autor: [Emanuel Malfatti](https://twitter.com/ejmalfatti)
