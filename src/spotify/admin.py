from django.contrib import admin
from spotify.models import Genre, Artist, Album, Track, SpotifyLink, FollowedArtist, SavedSpotifyLink


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'get_genres',)

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

    get_genres.short_description = 'Genres'


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'get_artists', 'get_genres',)
    search_fields = ('name', 'artist__name',)
    list_filter = ('album_type',)

    def get_artists(self, obj):
        return ", ".join([artist.name for artist in obj.artists.all()])

    def get_genres(self, obj):
        return ", ".join([genre.name for genre in obj.genres.all()])

    get_artists.short_description = 'Artists'
    get_genres.short_description = 'Genres'


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'album', 'get_artists', 'preview_url',)
    search_fields = ('name', 'album__name',)

    def get_artists(self, obj):
        return ", ".join([artist.name for artist in obj.artists.all()])

    get_artists.short_description = 'Artists'


@admin.register(SpotifyLink)
class SpotifyLinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'link_type', 'artist', 'album', 'track')
    list_filter = ('link_type',)


@admin.register(SavedSpotifyLink)
class SavedSpotifyLinkAdmin(admin.ModelAdmin):
    pass


@admin.register(FollowedArtist)
class FollowedArtistAdmin(admin.ModelAdmin):
    pass
