w outside users to add/edit/update data.</p>

## Details
<ul>
    <li> Management commands: </li>
        <p> Import: A command that can be used to import the data from the 2018 census file (in CSV format). The file path should be specified at the command line after the name of the management command.

  ```sh
  python manage.py import /path/to/file.csv
  ```
  Export: A command that can be used to export the data in CSV format. The file path should be specified at the command line after the name of the management command.

   ```sh
    python manage.py export /path/to/file.csv
   ```
   </p>

  <li> Views </li>
   <p>
    1.  A view that shows a map that displays the location of the squirrel sightings on an OpenStreets map.

         Located at: /map

         Methods Supported: GET

    2.  A view that lists all squirrel sightings with links to view each sighting

         Located at: /sightings

         Methods Supported: GET

    3.  A view to update a particular sighting

          Located at: /sightings


          Method: POST


    4.  A view to create a new sighting 

        
           Located at: /sightings/add


            Method: POST



    5.  A view to delete a sighting



           Located at: /sightings/



           Method: DELETE


    6. A view with general statistics about the sightings

           Located at: /sightings/stats
        
           Method: GET
                
  </p>
</ul>

## Data Source

We use squirrel data [**2018 Central Park Squirrel Census**](https://data.cityofnewyork.us/Environment/2018-Central-Park-Squirrel-Census-Squirrel-Data/vfnx-vebw) which was counted by the [**Squirrel Census**](https://www.thesquirrelcensus.com/). 

## Version Requirements
<ul>
    <li> Python 3.6+ </li>
    <li> Django 2.2 </li>
</ul>

## Reference Material
<ul>
    <li>https://docs.djangoproject.com/en/3.0/intro/tutorial01/</li>
    <li>https://docs.google.com/document/d/1SPv3fMDKiemrR86rD-S9ecvI2npz3PljDzwCfxK2x5g/edit</li>
</ul>

## Discussion and Development
<p>Most development discussions take place on github in this repo.</p>

## Contributing to Squirrel Tracking
<p>This is a project for the IEOR 4501 class. All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.</p>
</html>
  
