import json

# Custom serialization function
def custom_serializer(obj):
    if isinstance(obj, (int, float)):
        return obj  # Return the original value
    raise TypeError(f'Type {type(obj)} not serializable')

f = open('MIT_3D_Flood_Map/RELOAD-Ed.json')

# returns JSON object as
# a dictionary
data = json.load(f)

names = ["Model_ID", "Building_I", "Name", "POI_Type", "Model_Date", "Model_Sour", 
         "Ground_Ele", "Max_Elev_F", "Min_Elev_F", "Height_Ft", "Center_Lat", "Center_Lon", 
         "Google_Lin",	"Nearmap_Li", "Editor", "Edit_Date", "Edit_Note", "Tile", "Model_Cred", 
         "Status", "created_us", "created_da"]


for item in data['nodes']:
    try:
        properties = item["extras"]["properties"]

        tempdict = {}
        for n in range(len(names)):
            try:
                tempdict[names[n]] = float(properties[n])
            except:
                tempdict[names[n]] = properties[n]

        item["extras"] = tempdict

        with open('MIT_3D_Flood_Map/RELOAD-Ed.json', 'w') as file:
            json.dump(data, file, default=custom_serializer)
    except:
        break
