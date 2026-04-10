# Public APIs For Stan (No Auth)

## Important Reality Check

- Truly unlimited APIs are rare.
- Most "no auth" APIs still have fair-use or hidden throttling.
- For Stan, safest strategy is: cache responses, retry with backoff, and keep offline fallbacks.

## 1) Time, Location, Country Data

- World Time API
  - Endpoint: `https://worldtimeapi.org/api/timezone/Asia/Kolkata`
  - Use case: current time, timezone utilities.
  - Auth: none.

- REST Countries
  - Endpoint: `https://restcountries.com/v3.1/name/india`
  - Use case: country facts, flags, regional info.
  - Auth: none.

- Zippopotam
  - Endpoint: `https://api.zippopotam.us/in/400031`
  - Use case: pin/postal code lookup.
  - Auth: none.

## 2) Weather and Environment

- Open-Meteo
  - Endpoint: `https://api.open-meteo.com/v1/forecast?latitude=19.01&longitude=72.85&current=temperature_2m,weather_code`
  - Use case: weather cards and daily planning.
  - Auth: none.

- wttr.in
  - Endpoint: `https://wttr.in/Mumbai?format=j1`
  - Use case: quick weather summary in JSON.
  - Auth: none.

## 3) Education and Knowledge

- Open Library Search
  - Endpoint: `https://openlibrary.org/search.json?q=constitutional+law`
  - Use case: book suggestions for CLAT/MH-CET reading.
  - Auth: none.

- Wikipedia REST Summary
  - Endpoint: `https://en.wikipedia.org/api/rest_v1/page/summary/Indian_Constitution`
  - Use case: instant concept summaries.
  - Auth: none.

- Universities List API (Hipolabs)
  - Endpoint: `http://universities.hipolabs.com/search?country=India`
  - Use case: college discovery modules.
  - Auth: none.

## 4) Utility and Productivity

- QR Code Server
  - Endpoint: `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=hello`
  - Use case: generate QR from text/links.
  - Auth: none.

- HTTPBin
  - Endpoint: `https://httpbin.org/get`
  - Use case: API testing and debug panel.
  - Auth: none.

- JSONPlaceholder
  - Endpoint: `https://jsonplaceholder.typicode.com/todos/1`
  - Use case: demo/testing data for UI and parsing.
  - Auth: none.

## 5) Fun and Engagement

- Official Joke API
  - Endpoint: `https://official-joke-api.appspot.com/random_joke`
  - Use case: mood booster command.
  - Auth: none.

- Advice Slip API
  - Endpoint: `https://api.adviceslip.com/advice`
  - Use case: daily advice cards.
  - Auth: none.

- Cat Facts
  - Endpoint: `https://catfact.ninja/fact`
  - Use case: random fact command.
  - Auth: none.

## 6) Finance and Markets

- Frankfurter
  - Endpoint: `https://api.frankfurter.app/latest?from=INR&to=USD,EUR`
  - Use case: currency conversion command.
  - Auth: none.

- CoinGecko (Public)
  - Endpoint: `https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=inr`
  - Use case: crypto price checks.
  - Auth: none.

## 7) Language and Dictionary

- Dictionary API
  - Endpoint: `https://api.dictionaryapi.dev/api/v2/entries/en/focus`
  - Use case: vocabulary helper.
  - Auth: none.

- Datamuse
  - Endpoint: `https://api.datamuse.com/words?rel_syn=smart`
  - Use case: synonyms, word game tools.
  - Auth: none.

## 8) Translation (No-Auth Community Endpoint)

- LibreTranslate (public demo)
  - Endpoint: `https://libretranslate.de/translate`
  - Method: POST
  - JSON body example:
    {
      "q": "How are you?",
      "source": "en",
      "target": "hi",
      "format": "text"
    }
  - Use case: quick translation utility.
  - Auth: none on demo endpoints, but availability can vary.

## Integration Notes For Stan

- Add a timeout (5-10s) for every request.
- Cache last success result for each API command.
- Use command format like `/api weather mumbai` or `/api convert inr usd 100`.
- Show friendly fallback if endpoint is down.
- For low data plans, prefer short JSON endpoints and avoid large payloads.

## 9) Hacky + OSINT Style (No Auth)

- IPify
  - Endpoint: `https://api.ipify.org?format=json`
  - Use case: detect current public IP.
  - Auth: none.

- IPAPI
  - Endpoint: `https://ipapi.co/json/`
  - Use case: geo + ASN + network basics from IP.
  - Auth: none.

- Cloudflare Trace
  - Endpoint: `https://www.cloudflare.com/cdn-cgi/trace`
  - Use case: quick network diagnostics (colo, ip, protocol).
  - Auth: none.

- crt.sh Certificate Search
  - Endpoint: `https://crt.sh/?q=example.com&output=json`
  - Use case: subdomain discovery from TLS cert logs.
  - Auth: none.

- Wayback Availability
  - Endpoint: `https://archive.org/wayback/available?url=example.com`
  - Use case: check archived snapshots of websites.
  - Auth: none.

- URLhaus
  - Endpoint: `https://urlhaus-api.abuse.ch/v1/url/`
  - Method: POST (`url=<target_url>`)
  - Use case: basic malicious URL intelligence lookup.
  - Auth: none.

## 10) Maps, Geo, Nearby Search (No Auth)

- OpenStreetMap Nominatim Search
  - Endpoint: `https://nominatim.openstreetmap.org/search?q=wadala+mumbai&format=jsonv2`
  - Use case: geocoding place name to coordinates.
  - Auth: none.

- OpenStreetMap Nominatim Reverse
  - Endpoint: `https://nominatim.openstreetmap.org/reverse?lat=19.0176&lon=72.8562&format=jsonv2`
  - Use case: reverse geocoding coordinates to address.
  - Auth: none.

- Overpass API
  - Endpoint: `https://overpass-api.de/api/interpreter`
  - Method: POST (`data=<overpass_query>`)
  - Use case: nearby ATM, library, bus stops, drinking water, etc.
  - Auth: none.

- OpenTopoData
  - Endpoint: `https://api.opentopodata.org/v1/srtm90m?locations=19.0176,72.8562`
  - Use case: elevation lookup.
  - Auth: none.

- Sunrise-Sunset
  - Endpoint: `https://api.sunrise-sunset.org/json?lat=19.0176&lng=72.8562&formatted=0`
  - Use case: sunrise/sunset based routine planning.
  - Auth: none.

## 11) News, Research, Learning Feed (No Auth)

- Hacker News Algolia Search
  - Endpoint: `https://hn.algolia.com/api/v1/search?query=python`
  - Use case: latest dev/startup discussions.
  - Auth: none.

- StackExchange Search
  - Endpoint: `https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=votes&tagged=python&site=stackoverflow`
  - Use case: top answers for coding issues.
  - Auth: none.

- arXiv API
  - Endpoint: `https://export.arxiv.org/api/query?search_query=all:legal+reasoning&start=0&max_results=5`
  - Use case: research paper fetch and summary.
  - Auth: none.

- Crossref Works
  - Endpoint: `https://api.crossref.org/works?query=constitutional+law&rows=5`
  - Use case: journals/books metadata search.
  - Auth: none.

## 12) Government / Public Data (No Auth)

- Data.gov.in Catalog
  - Endpoint: `https://www.data.gov.in/`
  - Use case: discover Indian public datasets (many APIs need separate keys).
  - Auth: mixed.

- Nager.Date Holidays
  - Endpoint: `https://date.nager.at/api/v3/PublicHolidays/2026/IN`
  - Use case: public holidays planner.
  - Auth: none.

- USGS Earthquakes
  - Endpoint: `https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson`
  - Use case: earthquake feed for alerts panel.
  - Auth: none.

## 13) Space + Science + Sensor Style (No Auth)

- Where The ISS At
  - Endpoint: `https://api.wheretheiss.at/v1/satellites/25544`
  - Use case: live ISS tracker command.
  - Auth: none.

- Open Notify Astronauts
  - Endpoint: `http://api.open-notify.org/astros.json`
  - Use case: humans currently in space.
  - Auth: none (HTTP only endpoint).

- Open-Meteo Air Quality
  - Endpoint: `https://air-quality-api.open-meteo.com/v1/air-quality?latitude=19.01&longitude=72.85&hourly=pm10,pm2_5,ozone`
  - Use case: AQI-aware study/work suggestions.
  - Auth: none.

## 14) Media, Entertainment, and Creative Tools (No Auth)

- TVMaze
  - Endpoint: `https://api.tvmaze.com/search/shows?q=suits`
  - Use case: show tracker cards.
  - Auth: none.

- Jikan (MyAnimeList unofficial)
  - Endpoint: `https://api.jikan.moe/v4/anime?q=one%20piece&limit=3`
  - Use case: anime lookup and recommendations.
  - Auth: none.

- PokeAPI
  - Endpoint: `https://pokeapi.co/api/v2/pokemon/pikachu`
  - Use case: mini fun command/game mode.
  - Auth: none.

- Cataas
  - Endpoint: `https://cataas.com/cat?json=true`
  - Use case: mascot mood booster cards.
  - Auth: none.

## 15) Dev Tools and Scrappy Utilities (No Auth)

- DNS over HTTPS (Google)
  - Endpoint: `https://dns.google/resolve?name=example.com&type=A`
  - Use case: DNS checks inside Stan.
  - Auth: none.

- DNS over HTTPS (Cloudflare)
  - Endpoint: `https://cloudflare-dns.com/dns-query?name=example.com&type=A`
  - Use case: cross-verify DNS resolution.
  - Auth: none (send `accept: application/dns-json`).

- AllOrigins Proxy
  - Endpoint: `https://api.allorigins.win/get?url=https://example.com`
  - Use case: bypass CORS for fetch-based web snippets.
  - Auth: none.

- CountAPI
  - Endpoint: `https://api.countapi.xyz/hit/stan-v1/launches`
  - Use case: simple cloud counter for usage analytics.
  - Auth: none.

- OpenGraph Preview (Microlink)
  - Endpoint: `https://api.microlink.io/?url=https://example.com`
  - Use case: preview cards from links.
  - Auth: none.

## 16) High-Leverage Quick Command Ideas

- `/api ip`
  - Uses IPify + IPAPI + Cloudflare trace to show network diagnostics.

- `/api nearby atm wadala`
  - Geocode with Nominatim, search amenities with Overpass.

- `/api website snapshot example.com`
  - Check Wayback availability + fetch OpenGraph metadata.

- `/api threat-check https://...`
  - URLhaus lookup with safe fallback message.

- `/api env mumbai`
  - Open-Meteo weather + air-quality in one response.

- `/api holidays in 2026`
  - Nager.Date holiday feed.

## 17) Practical Warnings

- No-auth does not always mean no limits.
- Some public endpoints can change or disappear without notice.
- Keep per-command cooldown (for example 3-5 seconds) to avoid accidental spam.
- Save last valid response in local cache for offline-friendly behavior.

## 18) Extra API Pack (More Useful + Hacky)

### Jobs and Career

- Arbeitnow Jobs
  - Endpoint: `https://www.arbeitnow.com/api/job-board-api`
  - Use case: remote and international job feed cards.
  - Auth: none.

### Health and Safety Data

- Disease.sh
  - Endpoint: `https://disease.sh/v3/covid-19/all`
  - Use case: global health trend dashboard.
  - Auth: none.

- openFDA Drug Labels
  - Endpoint: `https://api.fda.gov/drug/label.json?limit=1`
  - Use case: medicine safety metadata exploration.
  - Auth: none.

### Games and Entertainment

- Open Trivia DB
  - Endpoint: `https://opentdb.com/api.php?amount=10`
  - Use case: quiz and practice mode.
  - Auth: none.

- CheapShark
  - Endpoint: `https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15`
  - Use case: low-budget game deal watcher.
  - Auth: none.

- FreeToGame
  - Endpoint: `https://www.freetogame.com/api/games`
  - Use case: free game discovery feed.
  - Auth: none.

- Chess.com Published Data API
  - Endpoint: `https://api.chess.com/pub/player/hikaru`
  - Use case: chess profile stats and recent activity links.
  - Auth: none.

### Science and Space

- SpaceX API
  - Endpoint: `https://api.spacexdata.com/v4/launches/latest`
  - Use case: launch mission feed.
  - Auth: none.

- NASA APOD (demo key)
  - Endpoint: `https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY`
  - Use case: astronomy wallpaper and learning cards.
  - Auth: demo key embedded in URL.

### Open Data and Utility

- Open Food Facts
  - Endpoint: `https://world.openfoodfacts.org/api/v0/product/737628064502.json`
  - Use case: barcode-based food info.
  - Auth: none.

- Open Brewery DB
  - Endpoint: `https://api.openbrewerydb.org/v1/breweries?by_city=mumbai`
  - Use case: open business-style location dataset.
  - Auth: none.

- RandomUser
  - Endpoint: `https://randomuser.me/api/`
  - Use case: mock profile generation for testing.
  - Auth: none.

### Transport and Mobility

- CityBikes
  - Endpoint: `https://api.citybik.es/v2/networks`
  - Use case: bike-sharing station/network data.
  - Auth: none.

- transport.rest Locations
  - Endpoint: `https://v6.db.transport.rest/locations?query=berlin&results=5`
  - Use case: transit stop search and travel helper prototypes.
  - Auth: none.

### Food and Daily Life

- TheMealDB
  - Endpoint: `https://www.themealdb.com/api/json/v1/1/search.php?s=dal`
  - Use case: recipe suggestions by ingredient/meal name.
  - Auth: none.

### Fun Boosters

- YesNo API
  - Endpoint: `https://yesno.wtf/api`
  - Use case: quick decision prompt cards.
  - Auth: none.

- Dog CEO
  - Endpoint: `https://dog.ceo/api/breeds/image/random`
  - Use case: random dog image mood boost.
  - Auth: none.

- xkcd
  - Endpoint: `https://xkcd.com/info.0.json`
  - Use case: daily geek comic in dashboard.
  - Auth: none.

## 19) Imported From Your New Source List

These are now integrated in Stan catalog (API Hub + custom workflows):

- API Directories
  - APIs.guru: `https://api.apis.guru/v2/list.json`

- Art and Image
  - Art Institute of Chicago: `https://api.artic.edu/api/v1/artworks/search?q={query}`
  - COLOURlovers: `https://www.colourlovers.com/api/colors/new?format=json`
  - DiceBear: `https://api.dicebear.com/6.x/pixel-art/svg?seed={seed}`
  - HTTP Cats: `https://http.cat/{status}`
  - Lorem Picsum: `https://picsum.photos/{width}/{height}`
  - RoboHash: `https://robohash.org/{text}.png`

- Content and Learning
  - HackerNews Firebase: `https://hacker-news.firebaseio.com/v0/item/{item_id}.json`
  - Reddit JSON: `https://www.reddit.com/r/{subreddit}/top.json?limit=10&t=week`
  - MediaWiki API: `https://en.wikipedia.org/w/api.php?action=query&prop=extracts&explaintext=1&titles={title}&format=json`
  - WordPress public posts: `https://{domain}/wp-json/wp/v2/posts?per_page=5&context=embed`

- Finance and Crypto
  - CoinDesk BPI: `https://api.coindesk.com/v1/bpi/currentprice.json`
  - CoinCap assets: `https://api.coincap.io/v2/assets`
  - Open ER API: `https://open.er-api.com/v6/latest/{base}`
  - Razorpay IFSC: `https://ifsc.razorpay.com/{ifsc}`

- Developer Tools
  - Agify: `https://api.agify.io?name={name}`
  - Genderize: `https://api.genderize.io?name={name}`
  - Nationalize: `https://api.nationalize.io?name={name}`
  - QuickChart: `https://quickchart.io/chart?c={chart}`
  - is.gd: `https://is.gd/create.php?format=simple&url={url}`
  - Unshorten: `https://unshorten.me/json/{shortcode}`

- Geo
  - Country.is: `https://api.country.is/{ip}`
  - GeoJS: `https://get.geojs.io/v1/ip/geo.json`
  - geocode.xyz: `https://geocode.xyz/{lat},{lon}?geoit=json`
  - Postcodes.io: `https://api.postcodes.io/postcodes/{postcode}`
  - ViaCEP: `https://viacep.com.br/ws/{cep}/json/`

- Government and Public Data
  - FBI Wanted: `https://api.fbi.gov/wanted/v1/list`
  - USAspending agencies: `https://api.usaspending.gov/api/v2/references/toptier_agencies/`

- Health
  - HealthCare.gov index: `https://www.healthcare.gov/api/index.json`
  - openFDA food enforcement: `https://api.fda.gov/food/enforcement.json?limit=10`

- Inspiration
  - Affirmations: `https://www.affirmations.dev/`
  - Quotable random: `https://api.quotable.io/quotes/random`

- Jobs
  - Jobicy remote jobs: `https://jobicy.com/api/v2/remote-jobs?count=20&geo={geo}&industry={industry}`

- Science and Space
  - Spaceflight News: `https://api.spaceflightnewsapi.net/v4/articles/?limit=10`
  - TheSpaceDevs agencies: `https://ll.thespacedevs.com/2.2.0/agencies/?limit=10`

- Sports and Weather
  - Ergast F1: `https://ergast.com/api/f1/drivers.json`
  - 7Timer Astro: `http://www.7timer.info/bin/api.pl?lon={lon}&lat={lat}&product=astro&output=json`
  - Aviation Weather: `https://aviationweather.gov/api/data/airport?ids={icao}`
  - openSenseMap: `https://api.opensensemap.org/boxes/{box_id}?format=json`

## Newly Imported Batch (Continuation)

- Games and Fun
  - AmiiboAPI: `https://www.amiiboapi.com/api/amiibo/?name={name}`
  - DND 5e API: `https://www.dnd5eapi.co/api/features/{index}`
  - Deck of Cards: `https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={deck_count}`
  - GamerPower: `https://www.gamerpower.com/api/giveaways?platform={platform}&sort-by=popularity`
  - BOTW Compendium: `https://botw-compendium.herokuapp.com/api/v2/entry/{entry}`
  - Chuck Norris Jokes: `https://api.chucknorris.io/jokes/random`

- Food and Recipes
  - CocktailDB: `https://www.thecocktaildb.com/api/json/v1/1/search.php?s={query}`

- Developer Utilities
  - APIC Agent UA parser: `https://api.apicagent.com/?ua={user_agent}`
  - Google favicon fetcher: `https://www.google.com/s2/favicons?domain={domain}&sz={size}`
  - Cloudflare trace alt: `https://1.1.1.1/cdn-cgi/trace`
  - goQR create endpoint: `https://api.qrserver.com/v1/create-qr-code/?data={text}&size={size}`

## Newly Imported Batch (Continuation 2)

- Geo
  - Ziptastic ZIP lookup: `https://ziptasticapi.com/{zipcode}`

- Government and Public Data
  - BrasilAPI holidays: `https://brasilapi.com.br/api/feriados/v1/{year}`
  - Dawum polls: `https://api.dawum.de/`
  - Federal Register document: `https://www.federalregister.gov/api/v1/documents/{document_number}`
  - Data USA population: `https://datausa.io/api/data?drilldowns=Nation&measures=Population&year={year}`
  - World Bank regions: `https://api.worldbank.org/v2/region?format=json`

- Health and Inspiration
  - Makeup API: `http://makeup-api.herokuapp.com/api/v1/products.json?brand={brand}`
  - NPPES provider search: `https://npiregistry.cms.hhs.gov/api/?version=2.1&city={city}`
  - Kanye quotes: `https://api.kanye.rest/`
  - Breaking Bad quotes: `https://api.breakingbadquotes.xyz/v1/quotes`
  - Quote Garden: `https://quote-garden.onrender.com/api/v3/quotes?limit={limit}`

- Music, Open Data, and Science
  - iTunes Search: `https://itunes.apple.com/search?term={query}`
  - MusicBrainz artist lookup: `https://musicbrainz.org/ws/2/artist/{mbid}?fmt=json`
  - Carbon Intensity UK: `https://api.carbonintensity.org.uk/intensity/date/{date}`
  - Police UK street crime: `https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lon}&date={date}`
  - NHTSA vehicle types: `https://vpic.nhtsa.dot.gov/api/vehicles/GetVehicleTypesForMake/{make}?format=json`
  - Wikimedia pageviews: `https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/{title}/daily/{start}/{end}`
  - Arcsecond activities: `https://api.arcsecond.io/activities/`
  - GBIF occurrence search: `https://api.gbif.org/v1/occurrence/search?year={year_start},{year_end}&limit=10`
  - Newton math: `https://newton.now.sh/api/v2/{operation}/{expression}`
  - Numbers API: `http://numbersapi.com/{number}/{kind}`

## Newly Imported Batch (Continuation 3)

- Transport
  - VBB transport locations: `https://v6.vbb.transport.rest/locations?query={query}`
  - iRail vehicle details: `https://api.irail.be/vehicle/?id={vehicle_id}&format=json&lang=en&alerts=false`

- Test Data
  - Bacon Ipsum: `https://baconipsum.com/api/?type={type}&paras={paras}`
  - FakerAPI credit cards: `https://fakerapi.it/api/v1/credit_cards?_quantity={quantity}`
  - Reqres users: `https://reqres.in/api/users?page={page}`
  - Restful API objects: `https://api.restful-api.dev/objects`
  - UUID tools generate: `https://www.uuidtools.com/api/generate/v1/count/{count}`

- Open Data and Science
  - Archive.org metadata: `https://archive.org/metadata/{identifier}`
  - Open Library ISBN: `https://openlibrary.org/api/volumes/brief/isbn/{isbn}.json`
  - CelesTrak GP: `https://celestrak.org/NORAD/elements/gp.php?INTDES={intdes}&FORMAT=JSON`
  - USGS FDSN query: `https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime={start}&endtime={end}&minmagnitude={minmag}`
  - SunriseSunset.io: `https://api.sunrisesunset.io/json?lat={lat}&lng={lon}&timezone={timezone}&date={date}`

## Newly Imported Batch (Continuation 4)

- Science and Space
  - arXiv search: `https://export.arxiv.org/api/query?search_query=all:{query}&start=0&max_results=5`
  - Asterank search: `http://www.asterank.com/api/skymorph/search?target={target}`
  - Cat Facts random: `https://cat-fact.herokuapp.com/facts/random`
  - Open Notify astronauts: `http://api.open-notify.org/astros.json`
  - SpaceX latest launch: `https://api.spacexdata.com/v5/launches/latest`
  - Spaceflight News latest: `https://api.spaceflightnewsapi.net/v3/articles`

- Transport and Weather
  - MBTA route patterns: `https://api-v3.mbta.com/route_patterns?filter[route]={route}&include=representative_trip&fields[trip]=headsign`
  - Metro Lisboa status: `https://app.metrolisboa.pt/status/getLinhas.php`
  - SG weather air temperature: `https://api.data.gov.sg/v1/environment/air-temperature`
  - wttr.in London: `https://wttr.in/London?format=3`

- Open Data
  - Open Government Canada package: `https://open.canada.ca/data/api/action/package_show?id={package_id}`
  - NYC Open Data record: `https://data.cityofnewyork.us/resource/{dataset}.json?{query_string}`
  - Open Data DC traffic: `https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Transportation_TrafficVolume_WebMercator/MapServer/171/query?where=1%3D1&outFields=ROUTEID,FROMMEASURE,TOMEASURE,FROMDATE,TODATE&outSR=4326&f=json`

## Newly Imported Batch (Continuation 5)

- Open Data and Media
  - Fipe models: `https://parallelum.com.br/fipe/api/v1/carros/marcas/{brand_id}/modelos`
  - House Stock Watcher: `https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/filemap.xml`
  - Leadsbox search: `https://leadsbox.biz/?query={query}`
  - PM2.5 latest: `https://pm25.lass-net.org/API-1.0.0/project/airbox/latest/`
  - OpenWhyd hot: `https://openwhyd.org/hot/{genre}?format=json`
  - Binary Jazz genre generator: `https://binaryjazz.us/wp-json/genrenator/v1/genre/{count}`

- Sports
  - Football-Data competitions: `https://api.football-data.org/v4/competitions/`
  - NHL standings: `https://api-web.nhle.com/v1/standings-season`

- Language and Test Data
  - PurgoMalum: `https://www.purgomalum.com/service/json?text={text}`
  - Loripsum: `https://loripsum.net/api/{paragraphs}/short/headers`
  - Softwium books: `https://softwium.com/api/books`
  - Chinese Character Web: `http://ccdb.hemiola.com/characters/radicals/{radical}?count`
  - Chinese Text Project: `https://api.ctext.org/getdictionaryheadwords`

<!-- markdownlint-disable -->
```text
i googled and found more see whag you can add

Big List of Free and Open Public APIs (No Auth Needed)
Last Updated on: January 6, 2026 by Ana
An API (Application Programming Interface) allows you to send and receive data from a remote server, like querying a database. This is helpful when you're building an app or pulling metrics for reporting, because it means you can focus on presenting information in a unique or useful manner, rather than developing the underlying data set. For example, most weather apps get their weather forecast data from a weather API, rather than building weather stations themselves. For more detailed information on how APIs work, see here.

While most APIs require access via API keys (which are similar to passwords), or have complex methods of authentication, there are also quite a few APIs with no requirements at all. This is especially useful for beginners, as it means you can start exploring different APIs right away. It is also useful for web developers looking to access a sample data set for testing.

Big List of Free Open APIs
The APIs below can be accessed using any method:

your web browser (just click on the sample URLs to load them)
any modern coding language
cURL for the command line
no-code API clients like Swagger, Postman, or Insomnia
Mixed Analytics' own API Connector for Google Sheets
Filter list by category, name, or description
#	CATEGORY	API NAME	DESCRIPTION	SAMPLE URL
1	API Directories	APIs.guru	OpenAPI API directory	https://api.apis.guru/v2/list.json
2	Art & Images	Art Institute of Chicago	Artwork from the museum	https://api.artic.edu/api/v1/artworks/search?q=cats
3	Art & Images	COLOURlovers	Color trends	https://www.colourlovers.com/api/colors/new?format=json
4	Art & Images	DiceBear	Generate random SVG avatars	https://api.dicebear.com/6.x/pixel-art/svg
5	Art & Images	Dogs	Random dog images	https://dog.ceo/api/breeds/image/random
6	Art & Images	HTTP Cats	Cat images for HTTP status codes	https://http.cat/401
7	Art & Images	Lorem Picsum	Placeholder images	https://picsum.photos/200/300
8	Art & Images	Metropolitan Museum of Art	Artwork from the museum	https://collectionapi.metmuseum.org/public/collection/v1/objects/100
9	Art & Images	PHP-Noise	Noise background image generator	https://php-noise.com/noise.php?hex=FFFFFF&json
10	Art & Images	Placebear	Pictures of bears for use as placeholders	https://placebear.com/200/300
11	Art & Images	Random Dog	Random dog images	https://random.dog/woof.json
12	Art & Images	RandomFox	Random pictures of foxes	https://randomfox.ca/floof/
13	Art & Images	ReSmush	Image compression and optimization	http://api.resmush.it/ws.php?img=http://www.resmush.it/assets/images/jpg_example_original.jpg&qlty=95
14	Art & Images	RoboHash	Generate unique images from text	https://robohash.org/onerobot.png
15	Art & Images	Vadivelu Status Codes	HTTP Codes with images	https://vadivelu.anoram.com/gif/200
16	Calendar	Nager.Date	Public holidays	https://date.nager.at/api/v2/publicholidays/2020/US
17	Calendar	UK Bank Holidays	UK bank holidays	https://www.gov.uk/bank-holidays.json
18	Content	4chan	4chan's read-only API	https://a.4cdn.org/boards.json
19	Content	Anime News Network	Anime/manga encyclopedia	https://cdn.animenewsnetwork.com/encyclopedia/api.xml?title=4658
20	Content	Ceska Televize	Czech television program data	https://www.ceskatelevize.cz/services-old/programme/xml/schedule.php?user=test&date=30.01.2024&channel=ct24
21	Content	Chronicling America	Historic US newspapers	https://chroniclingamerica.loc.gov/newspapers.json
22	Content	Crossref	Scholarly metadata	https://api.crossref.org/journals?query=pharmacy+health
23	Content	Final Space	Television show Final Space	https://finalspaceapi.com/api/v0/episode/
24	Content	HackerNews	Hacker News API	https://hacker-news.firebaseio.com/v0/item/8863.json
25	Content	Ice and Fire	Quantified and structured data from the universe of Ice and Fire	https://anapioficeandfire.com/api/characters/581
26	Content	Jikan	Unofficial MyAnimeList API	https://api.jikan.moe/v4/anime?q=naruto
27	Content	Listly	Top 10 lists	https://list.ly/api/v4/meta?url=http://google.com
28	Content	MCU-Countdown	When is the next MCU film?	https://www.whenisthenextmcufilm.com/api
29	Content	Mediawiki	Wikipedia page content and revisions	https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles=Pet_door&rvprop=content&format=json
30	Content	Open Library	Books and book-related data	https://openlibrary.org/search.json?q=the+lord+of+the+rings
31	Content	Reddit	Public content from Reddit	https://www.reddit.com/r/Wallstreetbets/top.json?limit=10&t=year
32	Content	Reddit Stocks	Top stocks from Wallstreetbets	https://tradestie.com/api/v1/apps/reddit
33	Content	Rick and Morty	Rick and Morty characters	https://rickandmortyapi.com/api/character/108
34	Content	STAPI	Star Trek information	https://stapi.co/api/v2/rest/spacecraft/search
35	Content	SWAPI	Star Wars information	https://swapi.dev/api/planets/3/?format=json
36	Content	The Rosary	Rosary prayers	https://the-rosary-api.vercel.app/v1/today
37	Content	TVMaze	TV show information	http://api.tvmaze.com/search/shows?q=golden girls
38	Content	Wolne Lektury	Search ebooks from wolnelektury.pl	https://wolnelektury.pl/api/authors/edgar-allan-poe/
39	Content	WordPress	Posts from any public WordPress site	https://techcrunch.com/wp-json/wp/v2/posts?per_page=100&context=embed
40	Crypto & Finance	Binance	24 hr crypto data	https://api4.binance.com/api/v3/ticker/24hr
41	Crypto & Finance	CoinBase	Currency codes and names	https://api.coinbase.com/v2/currencies
42	Crypto & Finance	CoinCap	Real time cryptocurrency prices	https://api.coincap.io/v2/assets
43	Crypto & Finance	CoinDesk	Bitcoin price index	https://api.coindesk.com/v1/bpi/currentprice.json
44	Crypto & Finance	CoinGecko	Cryptocurrency market data	https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd
45	Crypto & Finance	CoinLore	Cryptocurrency market data	https://api.coinlore.net/api/tickers/
46	Crypto & Finance	CoinMap	Crypto ATMs	https://coinmap.org/api/v1/venues/
47	Crypto & Finance	Coinpaprika	Cryptocurrency data	https://api.coinpaprika.com/v1/coins/btc-bitcoin
48	Crypto & Finance	Currency Rates	Currency exchange rates	https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies.json
49	Crypto & Finance	DEX Screener	Blockchain screener	https://api.dexscreener.com/latest/dex/search?q=WBNB%20USDC
50	Crypto & Finance	ExchangeRate-API	Exchange rates	https://open.er-api.com/v6/latest/USD
51	Crypto & Finance	GeckoTerminal	Crypto data	https://api.geckoterminal.com/api/v2/networks
52	Crypto & Finance	Gemini	Cryptocurrency market data	https://api.gemini.com/v2/ticker/btcusd
53	Crypto & Finance	Kraken	Crypto data	https://api.kraken.com/0/public/Trades?pair=ltcusd
54	Crypto & Finance	KuCoin	Crypto data	https://api.kucoin.com/api/v1/market/stats?symbol=BTC-USDT
55	Crypto & Finance	NBP Web	Currency exchange rates and gold prices	http://api.nbp.pl/api/cenyzlota/last/30/?format=json
56	Crypto & Finance	Nexchange	Cryptocurrency market data	https://api.n.exchange/en/api/v1/pair/
57	Crypto & Finance	OKX	Cryptocurrency market data	https://www.okx.com/api/v5/market/tickers?instType=SPOT
58	Crypto & Finance	Razorpay IFSC	Indian Financial Systems Codes	https://ifsc.razorpay.com/YESB0DNB002
59	Crypto & Finance	WazirX	Crypto data	https://api.wazirx.com/sapi/v1/tickers/24hr
60	Developer Tools	Agify	Predict age based on a name	https://api.agify.io?name=bella
61	Developer Tools	APIC Agent	Detect browser, OS, and device from user agent	https://api.apicagent.com/?ua=Mozilla/5.0%20(Macintosh;%20Intel%20Mac%20OS%20X%2010_15_5)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/89.0.4389.114%20Safari/537.36
62	Developer Tools	Arul's Public APIs	Get IP address	https://api.aruljohn.com/ip/json
63	Developer Tools	Cloudflare Trace	Get IP address, user agent, etc	https://1.1.1.1/cdn-cgi/trace
64	Developer Tools	Digital Ocean Status	DigitalOcean status	https://status.digitalocean.com/api/v2/summary.json
65	Developer Tools	FilterLists	Lists of filters used by ad blockers	http://filterlists.com/api/directory/lists
66	Developer Tools	Genderize.io	Predict gender based on a name	https://api.genderize.io?name=scott
67	Developer Tools	Google Favicons	Google's unofficial favicon fetcher	https://www.google.com/s2/favicons?domain=quora.com&sz=32
68	Developer Tools	goQR	Create and read QR codes	http://api.qrserver.com/v1/create-qr-code/?data=https://mixedanalytics.com&size=100x100
69	Developer Tools	HTTPBin	Inspect user agent and headers	http://httpbin.org/get
70	Developer Tools	Image-Charts	Chart images	https://image-charts.com/chart?cht=p3&chs=700x100&chd=t:60,40&chl=Hello|World&chan&chf=ps0-0,lg,45,ffeb3b,0.2,f44336,1|ps0-1,lg,45,8bc34a,0.2,009688,1
71	Developer Tools	IP2Location	Get public IP address	https://api.ip2location.io/
72	Developer Tools	IPify	Get public IP address	https://api.ipify.org?format=json
73	Developer Tools	is.gd	URL shortener	https://is.gd/create.php?format=simple&url=www.example.com
74	Developer Tools	Microlink	Retrieve metadata and screenshots from any URL	https://api.microlink.io/?url=https://github.com/microlinkhq
75	Developer Tools	Nationalize.io	Predict nationality based on a name	https://api.nationalize.io?name=michael
76	Developer Tools	QuickChart	Generate charts on-the-fly	https://quickchart.io/chart?c={type:'bar',data:{labels:[2019,2020,2021,2022, 2023],datasets:[{label:'Users',data:[120,60,50,180,120]}]}}
77	Developer Tools	Serialif Color	Get colors in different formats	https://color.serialif.com/aquamarine
78	Developer Tools	Sixdots	Google playstore analysis	https://storeapi.six-dots.app/last_updated_100
79	Developer Tools	Un-Shorten	Unshorten shortened URLs	https://unshorten.me/json/goo.gl/IGL1lE
80	Developer Tools	URLhaus	Receive and submit malware URLs	https://urlhaus-api.abuse.ch/v1/urls/recent/limit/3/
81	Food & Drink	Cocktail Database	Cocktail recipes	https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita
82	Food & Drink	Open Brewery DB	Breweries	https://api.openbrewerydb.org/breweries
83	Food & Drink	Open Food Facts	Data on food products	https://world.openfoodfacts.org/api/v0/product/737628064502.json
84	Food & Drink	Spoonacular	Comprehensive food API	https://api.spoonacular.com/recipes/complexSearch
85	Food & Drink	Whisky Hunter	Whisky auctions	https://whiskyhunter.net/api/auctions_data/?format=json
86	Fun & Games	AmiiboAPI	Nintendo Amiibo database	https://www.amiiboapi.com/api/amiibo/?name=mario
87	Fun & Games	Barter	Digital game libraries, wishlists and tradables	https://barter.vg/browse/cards/json
88	Fun & Games	Board Game Geek	Board games	https://boardgamegeek.com/xmlapi/search?search=frika
89	Fun & Games	CheapShark	Price comparison for digital games	https://www.cheapshark.com/api/1.0/deals?upperPrice=15
90	Fun & Games	Chuck Norris Jokes	Chuck Norris facts	https://api.chucknorris.io/jokes/random
91	Fun & Games	D&D 5th Edition	Official 5th Edition of Dungeons & Dragons	https://www.dnd5eapi.co/api/features
92	Fun & Games	Data Dragon	League of Legends champions API	https://ddragon.leagueoflegends.com/cdn/14.3.1/data/en_US/champion.json
93	Fun & Games	Deck of Cards	Simulate a deck of cards	https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1
94	Fun & Games	Evil Insult Generator	Generate insults	https://evilinsult.com/generate_insult.php?lang=en&type=json
95	Fun & Games	FreeToGame	Free-to-play games	https://www.freetogame.com/api/games?platform=pc
96	Fun & Games	Gamerpower	Free games and giveaways	https://www.gamerpower.com/api/giveaways?platform=steam&type=loot&sort-by=popularity
97	Fun & Games	Hyrule Compendium	The Legend of Zelda: BOTW	https://botw-compendium.herokuapp.com/api/v2/entry/white-maned_lynel
98	Fun & Games	icanhazdadjoke	Dad jokes	https://icanhazdadjoke.com/
99	Fun & Games	Imgflip	Popular memes	https://api.imgflip.com/get_memes
100	Fun & Games	isEven	Check if a number is even	https://api.isevenapi.xyz/api/iseven/12/
101	Fun & Games	JokeAPI	Jokes	https://v2.jokeapi.dev/joke/Any?safe-mode
102	Fun & Games	Magic: The Gathering	Cards and sets from MTG	https://api.magicthegathering.io/v1/sets
103	Fun & Games	Official Joke	Jokes	https://official-joke-api.appspot.com/random_joke
104	Fun & Games	Open Trivia DB	Trivia questions	https://opentdb.com/api.php?amount=10&category=17&difficulty=easy
105	Fun & Games	PokéAPI	Pokémon data	https://pokeapi.co/api/v2/pokemon/ditto
106	Fun & Games	Pokémon TCG	Pokémon card data	https://api.pokemontcg.io/v2/cards/xy1-1
107	Fun & Games	RuneScape	Runescape data	https://services.runescape.com/m=itemdb_rs/api/catalogue/items.json?category=9&alpha=c&page=1
108	Fun & Games	Scryfall	Magic: The Gathering card data	https://api.scryfall.com/cards/search?order=cmc&q=c:red%20pow=3
109	Fun & Games	TCGdex	Pokémon card data	https://api.tcgdex.net/v2/en/sets
110	Fun & Games	XIVAPI	Final Fantasy XIV	https://xivapi.com/Action/127
111	Fun & Games	xkcd	xkcd comics	http://xkcd.com/info.0.json
112	Fun & Games	Yes or No?	Randomly generate a yes or no image	https://yesno.wtf/api
113	Geo	Adresse	French addresses and geocoding	https://api-adresse.data.gouv.fr/search/?q=8+bd+du+port
114	Geo	Country.is	Lookup country by IP address	https://api.country.is/9.9.9.9
115	Geo	Geocode	Forward/reverse geocoding	https://geocode.xyz/51.50354,-0.12768?geoit=json
116	Geo	GeoJS	Geolocation by IP address	https://get.geojs.io/v1/ip/geo.json
117	Geo	geoPlugin	Currency conversion and geolocation data	http://www.geoplugin.net/php.gp
118	Geo	GetTheData	UK geo coordinates conversion	https://api.getthedata.com/bng2latlong/529090/179645
119	Geo	HelloSalut	Translate "hello" by IP address	http://stefanbohacek.com/hellosalut/?mode=auto
120	Geo	Hong Kong GeoData Store	Hong Kong geo data	https://geodata.gov.hk/gs/api/v1.0.0/locationSearch?q=museums
121	Geo	ipapi	Geolocation by IP address	https://ipapi.co/json/
122	Geo	IPGeo	Geolocation by IP address	https://api.techniknews.net/ipgeo/
123	Geo	Nominatum	Locations and addresses	https://nominatim.openstreetmap.org/search.php?city=taipei&format=jsonv2
124	Geo	Open Topo Data	Determine elevation for lat/long	https://api.opentopodata.org/v1/srtm90m?locations=-43.5,172.5|27.6,1.98&interpolation=cubic
125	Geo	Postcodes	UK geo data by postcode	https://api.postcodes.io/postcodes/OX49%205NU
126	Geo	ViaCEP	Brazil's postal address codes (CEPs)	https://viacep.com.br/ws/01001000/json/
```
<!-- markdownlint-enable -->
127	Geo	Zippopotamus	Zip code information for 60 countries	https://api.zippopotam.us/us/90210
128	Geo	Ziptastic	US geo data by zipcode	https://ziptasticapi.com/90210
129	Government	Banco Central Do Brasil	Brazil Central Bank data	https://api.bcb.gov.br/dados/serie/bcdata.sgs.20716/dados/ultimos/10?formato=json
130	Government	Belgian Open Data Initiative	Belgian government open data	https://social.brussels/rest/sector/5/organisations
131	Government	Brasil	Brazil public data	https://brasilapi.com.br/api/feriados/v1/2024
132	Government	CiviX	Law and bylaw content of British Columbia	https://www.bclaws.gov.bc.ca/civix/search/complete/fullsearch?q=water&s=0&e=20&nFrag=5&lFrag=100
133	Government	Colorado Information Marketplace	Colorado state open data	https://data.colorado.gov/resource/4ykn-tg5h.json
134	Government	Data USA	US public data	https://datausa.io/api/data?drilldowns=Nation&measures=Population
135	Government	Data.gov	U.S. government open data	https://data.ny.gov/api/views/d6yy-54nr/rows.xml?accessType=DOWNLOAD
136	Government	Data.gov.au	Australian government open data	https://www.data.act.gov.au/api/views/s4g9-ndv2/rows.json?accessType=DOWNLOAD
137	Government	Dawum	German election polls	https://api.dawum.de/
138	Government	European Commission Taxation and Customs	Europan Comission taxes	https://ec.europa.eu/taxation_customs/vies/rest-api/ms/DE/vat/122268496
139	Government	FBI Wanted	FBI Wanted data	https://api.fbi.gov/wanted/v1/list
140	Government	Federal Register	Daily journal of the US government	https://www.federalregister.gov/api/v1/documents/2023-05167?publication_date=2023-03-14
141	Government	Food Standards Agency	UK restaurant hygiene ratings	https://ratings.food.gov.uk/OpenDataFiles/FHRS529en-GB.json
142	Government	NYC Open Data	New York City open data	https://data.cityofnewyork.us/resource/erm2-nwe9.json?unique_key=57056073
143	Government	Open Data DC	Washington DC open data	https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Transportation_TrafficVolume_WebMercator/MapServer/171/query?where=1%3D1&outFields=ROUTEID,FROMMEASURE,TOMEASURE,FROMDATE,TODATE&outSR=4326&f=json
144	Government	Open Government, Canada	Canadian government open data	https://open.canada.ca/data/api/action/package_show?id=5953da6b-d81b-4a2c-8b27-145892827fb0
145	Government	Represent Civic Information	Canada's elected officials and electoral districts	https://represent.opennorth.ca/representatives/?first_name=Jack
146	Government	USAspending	U.S. federal government spending data	https://api.usaspending.gov/api/v2/references/toptier_agencies/
147	Government	USPTO	US Patent and Trademark Office	https://developer.uspto.gov/ipmarketplace-api/search/query?searchText=vehicles
148	Government	World Bank	World Bank open data	http://api.worldbank.org/v2/region?format=json
149	Health	HealthCare.gov	US health insurance data	https://www.healthcare.gov/api/index.json
150	Health	Makeup	Makeup brands and product info	http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline
151	Health	NPPES	US health care providers	https://npiregistry.cms.hhs.gov/api/?version=2.1&city=baltimore
152	Health	openFDA	Food & Drug Administration data (US)	https://api.fda.gov/food/enforcement.json?limit=10
153	Inspiration	Advice Slip	Generate random advice	https://api.adviceslip.com/advice/search/love
154	Inspiration	Affirmations	Generate affirmations	https://www.affirmations.dev/
155	Inspiration	Breaking Bad Quotes	Retrieve some quotes of Breaking Bad	https://api.breakingbadquotes.xyz/v1/quotes
156	Inspiration	Dictum	Inspiring expressions	https://api.fisenko.net/v1/quotes/en?query=string&offset=0&limit=0
157	Inspiration	Game of Thrones Quotes	Retrieve some quotes of Game of Thrones	https://api.gameofthronesquotes.xyz/v1/random
158	Inspiration	Kanye	Kanye quotes	https://api.kanye.rest/
159	Inspiration	Quotable	Random quotes	https://api.quotable.io/quotes/random
160	Inspiration	Quote Garden	Database of 75000 quotes	https://quote-garden.onrender.com/api/v3/quotes
161	Inspiration	Quotes on Design	Quotes about design	https://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand
162	Inspiration	Ron Swanson Quotes	Ron Swanson quotes API	https://ron-swanson-quotes.herokuapp.com/v2/quotes
163	Jobs	Jobicy	List of remote jobs	https://jobicy.com/api/v2/remote-jobs?count=20&geo=usa&industry=marketing&tag=seo
164	Language	Chinese Character Web	Information about Chinese characters	http://ccdb.hemiola.com/characters/radicals/85?count
165	Language	Chinese Text Project	Digital library for pre-modern Chinese texts	https://api.ctext.org/getdictionaryheadwords
166	Language	Datamuse	Query words matching conditions	https://api.datamuse.com/words?ml=ringing+in+the+ears
167	Language	Free Dictionary	Word definitions and phonetics	https://api.dictionaryapi.dev/api/v2/entries/en/digital
168	Language	PurgoMalum	Check content for profanity	https://www.purgomalum.com/service/json?text=this%20is%20some%20test%20input
169	Music	Binary Jazz	Fetch a random genre	https://binaryjazz.us/wp-json/genrenator/v1/genre/5
170	Music	iTunes Search	iTunes content	https://itunes.apple.com/search?term=radiohead
171	Music	MusicBrainz	Music data	http://musicbrainz.org/ws/2/artist/5b11f4ce-a62d-471e-81fc-a69a8278c7da?fmt=json
172	Music	Openwhyd	Playlists from various streaming platforms	https://openwhyd.org/hot/electro?format=json
173	Open Data	Archive.org	Large public digital archive	https://archive.org/metadata/TheAdventuresOfTomSawyer_201303
174	Open Data	Carbon Intensity	Carbon intensity of the electricity system in Great Britain	https://api.carbonintensity.org.uk/intensity/date
175	Open Data	Data.Police.UK	UK crime & police data	https://data.police.uk/api/crimes-street/all-crime?lat=52.629729&lng=-1.131592&date=2023-01
176	Open Data	Fipe	Brazilian vehicles and prices	https://parallelum.com.br/fipe/api/v1/carros/marcas/59/modelos
177	Open Data	House Stock Watcher	US Congress members' stock transactions	https://house-stock-watcher-data.s3-us-west-2.amazonaws.com/data/filemap.xml
178	Open Data	Leadsbox	71 Million business records in 202 countries	https://leadsbox.biz/?query=lawyers+in+germany
179	Open Data	Open Library	Information about books	http://openlibrary.org/api/volumes/brief/isbn/9780525440987.json
180	Open Data	PM2.5	PM2.5 environmental data monitoring	https://pm25.lass-net.org/API-1.0.0/project/airbox/latest/
181	Open Data	Universities List	Universities	http://universities.hipolabs.com/search?country=United+Kingdom
182	Open Data	Vehicles	National Highway Traffic Safety Administration's catalog of vehicles specs	https://vpic.nhtsa.dot.gov/api/vehicles/GetVehicleTypesForMake/merc?format=json
183	Open Data	Wayback Machine	Internet archive availability	https://archive.org/wayback/available?url=google.com
184	Open Data	Wikipedia	Pageview stats	https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/all-agents/Tiger_King/daily/20210901/20210930
185	Science	Arcsecond	Worldwide astronomy data	https://api.arcsecond.io/activities/
186	Science	arXiv	Research-sharing platform	http://export.arxiv.org/api/query?search_query=all:electron
187	Science	Asterank	Asteroids, minor planets, and other objects	http://www.asterank.com/api/skymorph/search?target=J99TS7A
188	Science	Cat-Facts	Daily cat facts	https://cat-fact.herokuapp.com/facts/random
189	Science	CelesTrak	General perturbations orbital data	https://celestrak.org/NORAD/elements/gp.php?INTDES=2023-015&FORMAT=JSON-PRETTY
190	Science	GBIF	Global Biodiversity Information Facility	https://api.gbif.org/v1/occurrence/search?year=1800,1899
191	Science	iDigBio	Digitized data for millions of biological specimens	https://search.idigbio.org/v2/search/records/?rq={"data.dwc:dynamicProperties":"nsf_tcn"}&limit=1
192	Science	ITIS	Integrated Taxonomic Information System	https://www.itis.gov/ITISWebService/services/ITISService/searchByCommonName?srchKey=ferret-badger
193	Science	NASA	National Aeronautics and Space Administration	https://api.nasa.gov/neo/rest/v1/neo/browse?api_key=DEMO_KEY
194	Science	Newton	Advanced math	https://newton.now.sh/api/v2/factor/x^2-1
195	Science	Numbers	Facts about numbers	http://numbersapi.com/random/math
196	Science	Open Notify	ISS location and people in space	http://api.open-notify.org/astros.json
197	Science	Spaceflight News	Spaceflight related news	https://api.spaceflightnewsapi.net/v3/articles
198	Science	SpaceX	Launch and rocket data	https://api.spacexdata.com/v5/launches/latest
199	Science	SunriseSunset	Sunrise and sunset times	https://api.sunrisesunset.io/json?lat=38.907192&lng=-77.036873&timezone=UTC&date=today
200	Science	TheSpaceDevs	Rocket launches, space events and crewed spaceflight	https://ll.thespacedevs.com/2.2.0/agencies/?limit=10
201	Science	USGS Earthquake Catalog	Latest earthquakes	https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&starttime=2023-03-01&endtime=2023-03-02&minmagnitude=5
202	Sports	CityBikes	Bike sharing networks	http://api.citybik.es/v2/networks
203	Sports	Ergast F1	Motor racing data	http://ergast.com/api/f1/drivers.json
204	Sports	Football-Data	Football (soccer) competitions and data	http://api.football-data.org/v4/competitions/
205	Sports	nhlapi	NHL data	https://api-web.nhle.com/v1/standings-season
206	Test Data	Bacon Ipsum	Generate fake data for testing	https://baconipsum.com/api/?type=meat-and-filler
207	Test Data	Faker	Generate fake data	https://fakerapi.it/api/v1/credit_cards?_quantity=2
208	Test Data	JSONPlaceholder	Fake REST API for testing	https://jsonplaceholder.typicode.com/posts/1
209	Test Data	Loripsum	Generate fake placeholder text	https://loripsum.net/api/10/short/headers
210	Test Data	RandomUser	Fake user data generator	https://randomuser.me/api/
211	Test Data	Reqres	Test against a real API	https://reqres.in/api/users?page=1
212	Test Data	REST	Rest API for testing	https://api.restful-api.dev/objects
213	Test Data	Softwium	Dummy JSON data for a variety of categories	https://softwium.com/api/books
214	Test Data	UUID Generator	Generate UUIDs and GUIDs	https://www.uuidtools.com/api/generate/v1/count/3
215	Transportation	Derhuerst	Public transport for Berlin & Brandenburg	https://v6.vbb.transport.rest/locations?query=berlin
216	Transportation	iRail	Belgian railways	https://api.irail.be/vehicle/?id=BE.NMBS.IC1832&format=json&lang=en&alerts=false
217	Transportation	MBTA	Public transport for Boston	https://api-v3.mbta.com/route_patterns?filter[route]=CR-Providence&include=representative_trip&fields[trip]=headsign
218	Transportation	Metro Lisboa	Subway line status	https://app.metrolisboa.pt/status/getLinhas.php
219	Weather	7Timer!	Weather forecasts for astronomy	http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=astro&output=json
220	Weather	Aviation Weather Center	Aviation Digital Data Service (ADDS) data	https://aviationweather.gov/api/data/airport?ids=KMCI
221	Weather	Open-Meteo	Open source weather API	https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=temperature_2m_max,temperature_2m_min
222	Weather	openSenseMap	Personal senseBox (weather station) data	https://api.opensensemap.org/boxes/57000b8745fd40c8196ad04c?format=json
223	Weather	SG Weather	Realtime weather readings for Singapore	https://api.data.gov.sg/v1/environment/air-temperature
224	Weather	wttr	Console-oriented weather forecast service	wttr.in/London?format=3
Have another API for this list? Please submit it here.
CategoriesAPIs, Reporting
Leverage Enhanced Ecommerce Data Layer for Marketing Pixels
Scroll Tracking for Single-Page Applications (GTM)
147 thoughts on “Big List of Free and Open Public APIs (No Auth Needed)”
