from typing import Dict

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

tram_route_coordinates = {
    1: {"latitude": -34.9210, "longitude": 138.6106},
    2: {"latitude": -34.9211, "longitude": 138.6091},
    3: {"latitude": -34.9211, "longitude": 138.6077},
    4: {"latitude": -34.9212, "longitude": 138.6063},
    5: {"latitude": -34.9212, "longitude": 138.6050},
    6: {"latitude": -34.9213, "longitude": 138.6031},
    7: {"latitude": -34.9214, "longitude": 138.6024},
    8: {"latitude": -34.9214, "longitude": 138.6009},
    9: {"latitude": -34.9216, "longitude": 138.5995},
    10: {"latitude": -34.9229, "longitude": 138.5996},
    11: {"latitude": -34.9233, "longitude": 138.5995},
    12: {"latitude": -34.9243, "longitude": 138.5996},
    13: {"latitude": -34.9243, "longitude": 138.5997},
    14: {"latitude": -34.9257, "longitude": 138.5998},
    15: {"latitude": -34.9263, "longitude": 138.5997},
    16: {"latitude": -34.9277, "longitude": 138.6004},
    17: {"latitude": -34.9285, "longitude": 138.6007},
    18: {"latitude": -34.9290, "longitude": 138.6007},
    19: {"latitude": -34.9293, "longitude": 138.6005},
    20: {"latitude": -34.9300, "longitude": 138.6001},
    21: {"latitude": -34.9308, "longitude": 138.6001},
    22: {"latitude": -34.9315, "longitude": 138.6002},
    23: {"latitude": -34.9321, "longitude": 138.6002},
    24: {"latitude": -34.9332, "longitude": 138.6003},
    25: {"latitude": -34.9346, "longitude": 138.6004},
    26: {"latitude": -34.9356, "longitude": 138.6005},
    27: {"latitude": -34.9355, "longitude": 138.6017},
    28: {"latitude": -34.9355, "longitude": 138.6029},
    29: {"latitude": -34.9355, "longitude": 138.6039},
    30: {"latitude": -34.9354, "longitude": 138.6056},
    31: {"latitude": -34.9353, "longitude": 138.6065},
    32: {"latitude": -34.9352, "longitude": 138.6083},
    33: {"latitude": -34.9350, "longitude": 138.6120},
    34: {"latitude": -34.9350, "longitude": 138.6124},
    35: {"latitude": -34.9346, "longitude": 138.6124},
    36: {"latitude": -34.9340, "longitude": 138.6124},
    37: {"latitude": -34.9333, "longitude": 138.6123},
    38: {"latitude": -34.9332, "longitude": 138.6123},
    39: {"latitude": -34.9328, "longitude": 138.6122},
    40: {"latitude": -34.9323, "longitude": 138.6122},
    41: {"latitude": -34.9315, "longitude": 138.6122},
    42: {"latitude": -34.9312, "longitude": 138.6122},
    43: {"latitude": -34.9308, "longitude": 138.6121},
    44: {"latitude": -34.9295, "longitude": 138.6120},
    45: {"latitude": -34.9287, "longitude": 138.6120},
    46: {"latitude": -34.9284, "longitude": 138.6120},
    47: {"latitude": -34.9268, "longitude": 138.6118},
    48: {"latitude": -34.9256, "longitude": 138.6118},
    49: {"latitude": -34.9251, "longitude": 138.6118},
    50: {"latitude": -34.92452985179964, "longitude": 138.61128829550157},
    51: {"latitude": -34.924244283191385, "longitude": 138.61101422861762},
    52: {"latitude": -34.92239976689327, "longitude": 138.61081153328126},
    53: {"latitude": -34.921646031288795, "longitude": 138.6107458714139},
    54: {"latitude": -34.9210, "longitude": 138.6106},
}

bus_route_coordinates = {
    1: {"latitude": -34.90394175461262, "longitude": 138.5857860733029},
    2: {"latitude": -34.904233519490724, "longitude": 138.58560841647588},
    3: {"latitude": -34.904403042942036, "longitude": 138.58567178696035},
    4: {"latitude": -34.90480148355233, "longitude": 138.58580003677082},
    5: {"latitude": -34.905109593134696, "longitude": 138.58592376011302},
    6: {"latitude": -34.90554635835976, "longitude": 138.58607151190174},
    7: {"latitude": -34.90602027313525, "longitude": 138.58623144694226},
    8: {"latitude": -34.90631847920622, "longitude": 138.5863476261772},
    9: {"latitude": -34.907511163454835, "longitude": 138.5867687824025},
    10: {"latitude": -34.90775100464026, "longitude": 138.58686089650158},
    11: {"latitude": -34.908007841668905, "longitude": 138.58696913056295},
    12: {"latitude": -34.90818630516237, "longitude": 138.58703591328577},
    13: {"latitude": -34.908561171657674, "longitude": 138.58716141874112},
    14: {"latitude": -34.908859552834066, "longitude": 138.58727310708647},
    15: {"latitude": -34.90920231214944, "longitude": 138.58739976397737},
    16: {"latitude": -34.909955046156846, "longitude": 138.5877339479863},
    17: {"latitude": -34.91018148961414, "longitude": 138.58780966172438},
    18: {"latitude": -34.91054589828344, "longitude": 138.58797375313043},
    19: {"latitude": -34.91054671459939, "longitude": 138.58799366214345},
    20: {"latitude": -34.91056712249926, "longitude": 138.5880961935811},
    21: {"latitude": -34.910541000386345, "longitude": 138.5883420699596},
    22: {"latitude": -34.91049447035247, "longitude": 138.58852125111275},
    23: {"latitude": -34.91047406243367, "longitude": 138.5886436915843},
    24: {"latitude": -34.91040875706138, "longitude": 138.5888915588633},
    25: {"latitude": -34.91034018636399, "longitude": 138.5891862123375},
    26: {"latitude": -34.910290390940155, "longitude": 138.58933453454662},
    27: {"latitude": -34.91020631007523, "longitude": 138.58970583774058},
    28: {"latitude": -34.910090748689385, "longitude": 138.59015973751164},
    29: {"latitude": -34.91000748394061, "longitude": 138.59053004528144},
    30: {"latitude": -34.909908931627974, "longitude": 138.5909825635218},
    31: {"latitude": -34.90979709537668, "longitude": 138.59146933902403},
    32: {"latitude": -34.909596482568965, "longitude": 138.5923589178314},
    33: {"latitude": -34.90948684113118, "longitude": 138.5931049021683},
    34: {"latitude": -34.90922519786247, "longitude": 138.59427098875585},
    35: {"latitude": -34.909085653555806, "longitude": 138.59486808013165},
    36: {"latitude": -34.908742522923305, "longitude": 138.5963245607352},
    37: {"latitude": -34.90863134977847, "longitude": 138.5967805562329},
    38: {"latitude": -34.90824982260114, "longitude": 138.5966234226633},
    39: {"latitude": -34.90783292003011, "longitude": 138.5964786132823},
    40: {"latitude": -34.90730414215135, "longitude": 138.59627364203337},
    41: {"latitude": -34.9068772935041, "longitude": 138.59612632391406},
    42: {"latitude": -34.90649408713273, "longitude": 138.59598592164517},
    43: {"latitude": -34.90598494163197, "longitude": 138.5957884809463},
    44: {"latitude": -34.90555776973043, "longitude": 138.59564784509425},
    45: {"latitude": -34.90500903762534, "longitude": 138.59547453604182},
    46: {"latitude": -34.90462041846969, "longitude": 138.59532533428637},
    47: {"latitude": -34.903953276526664, "longitude": 138.59507742069889},
    48: {"latitude": -34.90353064932921, "longitude": 138.59494380633993},
    49: {"latitude": -34.903113878465575, "longitude": 138.5947984658346},
    50: {"latitude": -34.90269043710332, "longitude": 138.59465617443718},
    51: {"latitude": -34.902375355302134, "longitude": 138.59454132494804},
    52: {"latitude": -34.90200298160923, "longitude": 138.59442328508717},
    53: {"latitude": -34.902006620495094, "longitude": 138.59419940458486},
    54: {"latitude": -34.90207247131924, "longitude": 138.59389449444893},
    55: {"latitude": -34.90220500636156, "longitude": 138.5933314270724},
    56: {"latitude": -34.90222667873845, "longitude": 138.5932277576099},
    57: {"latitude": -34.90228919517693, "longitude": 138.5929635021704},
    58: {"latitude": -34.9023508780187, "longitude": 138.59268908300706},
    59: {"latitude": -34.90240672595655, "longitude": 138.59247259677915},
    60: {"latitude": -34.90253509271251, "longitude": 138.5918983493584},
    61: {"latitude": -34.90260344376069, "longitude": 138.5916036028705},
    62: {"latitude": -34.90268513152375, "longitude": 138.59124889072547},
    63: {"latitude": -34.902770986943835, "longitude": 138.59090027676928},
    64: {"latitude": -34.902886849937595, "longitude": 138.5903839622951},
    65: {"latitude": -34.90296353615022, "longitude": 138.5899967263508},
    66: {"latitude": -34.90309356912393, "longitude": 138.58946618269852},
    67: {"latitude": -34.903249441713804, "longitude": 138.58876895481475},
    68: {"latitude": -34.90340948171275, "longitude": 138.58805851416437},
    69: {"latitude": -34.903518675489316, "longitude": 138.58761741081304},
    70: {"latitude": -34.90363620450631, "longitude": 138.58706653980835},
    71: {"latitude": -34.9037303943071, "longitude": 138.5866955657753},
    72: {"latitude": -34.90384542241257, "longitude": 138.58619754584092},
    73: {"latitude": -34.90395378207309, "longitude": 138.58575745889738},
}


# Define the request body model
class CoordinateCreate(BaseModel):
    latitude: float
    longitude: float


# Define the API endpoints
@app.post("/tram_coordinates", response_model=Dict[str, float])
def get_tram_coordinate(coordinate: CoordinateCreate):
    tram_coordinate_id = len(tram_route_coordinates) + 1
    tram_route_coordinates[tram_coordinate_id] = {"latitude": coordinate.latitude,
                                                  "longitude": coordinate.longitude}
    return tram_route_coordinates[tram_coordinate_id]


@app.get("/tram_coordinates", response_model=Dict[int, Dict[str, float]])
def read_tram_coordinates():
    return tram_route_coordinates


@app.post("/bus_coordinates", response_model=Dict[str, float])
def get_bus_coordinate(coordinate: CoordinateCreate):
    bus_coordinate_id = len(bus_route_coordinates) + 1
    bus_route_coordinates[bus_coordinate_id] = {"latitude": coordinate.latitude,
                                                "longitude": coordinate.longitude}
    return bus_route_coordinates[bus_coordinate_id]


@app.get("/bus_coordinates", response_model=Dict[int, Dict[str, float]])
def read_bus_coordinates():
    return bus_route_coordinates


# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
