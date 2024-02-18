# thanks chatgpt and this article I saw :3
from datetime import datetime
from geopy import Photon
from tzwhere import tzwhere
from pytz import timezone, utc
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from skyfield.api import Star, load, wgs84
from skyfield.data import hipparcos
from skyfield.projections import build_stereographic_projection

# loading earth and star data
eph = load('de421.bsp')
# de421 is the ephemeris. i thought eph meant like ephelion
with load.open(hipparcos.URL) as f:
    stars = hipparcos.load_dataframe(f)

# geopy stuff 
location = 'Torrey Park, Torrey, UT'
# reason for location: idk buzzfeed said it was the city w the least light pollution LOL
when = '2024-01-01 17:07'
# reason for this specific time: astronomical twilight (time where stars are most visible) begins about 1 hr to 1 1/2 hrs after sunset for mid latitudes (torrey's latitude is 38 degrees, mid latitudes are 30-60)
# during astronomical twilight, sun's centroid is 18 degrees below horizon

geolocator = Photon(user_agent='OpenStreetMap')
location = geolocator.geocode('100 North 75 East, Torrey, UT 84775')
lat = location.latitude
long = location.longitude
print('The latitude of the skymap location is: ', lat, ', and the longtitude of the skymap location is: ', long)

# getting tz of torrey with pytz and tzwhere

# here we're defining dt to convert to utc based on the location's tz
dt = datetime.strptime(when, '%Y-%m-%d %H:%M')
timezone_str = tzwhere.tzwhere().tzNameAt(lat, long)
local = timezone(timezone_str)

local_dt = local.localize(dt, is_dst=None)
utc_dt = local_dt.astimezone(utc)

# okay now we have to define position of observer w skyfield library determines the sky the map will see) + location and time of observation
sun = eph['sun']
earth = eph['earth']

ts = load.timescale()
t = ts.from_datatime(utc_dt)

# defining observer (this sounds so ominous)
observer = wgs84.latlon(latitude_degrees=lat, longitude_degrees=long).at(t)
position = observer.from_altaz(alt_degrees=90, az_degrees=0)
# i have to look at horizontal coordinate system on the wiki or smth because idk what azimuth is

# the article says it isn't necessary to define the observer position .. but its ok in case I wanna change it

# fun part: calculating star positions with skyfield

# making a fake star here:
ra, dec, distance = observer.radec()
# equatorial ra is distances from center of planter to its equator
center_object = Star(ra=ra, dec=dec)

# stereographic projection: converts a projection of the sphere (in this context, I think it's earth) into a 2d plane
center = earth.at(t).observe(center_object)
projection = build_stereographic_projection(center)

star_positions = earth.at(t).observe(Star.from_dataframe(stars))
stars['x'], stars['y'] = projection(star_positions)

# building star chart with matplot library, yay (oh god math that's above my knowledge)
chart_size = 10 # this is in inches so it's 10x10
max_star_size = 100
limiting_magnitude = 10 # magnitude is brightness of stars 

bright_stars = (stars.magnitude <= limiting_magnitude)
magnitude = stars['magnitude'][bright_stars]

# formatting how the chart will look 
fig, ax = plt.subplots(figsize=(chart_size, chart_size))
border = plt.Circle((0, 0), 1, color='navy', fill=True)
ax.add_patch(border)
marker_size = max_star_size * 10 ** (magnitude / -2.5)

# scatterplot creation w the stars and their x&y locations, marker size = brightness
ax.scatter(stars['x'][bright_stars], stars['y'][bright_stars], s=marker_size, color='white', marker='.', linewidths=0, zorder=2) # marker has no outline and zorder=2 so stars are on top of the circle (z-order is order of which 2d objects appear)

# clip the horizon (I think this means limiting how much of the horizon is shown. I'm not sure tho)

horizon = Circle((0, 0), radius=1, transform=ax.transData)
for col in ax.collecctions:
    col.set_clip_path(horizon)

ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
plt.axis('off')

plt.show() # :D