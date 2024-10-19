from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def who(request):
    return HttpResponse("where is your house")

def subash(request):
    volume_of_wall = 0
    volume_of_brick=0
    total_number_of_bricks=0   

    if request.method =='POST':
        lengthofwall = float(request.POST['lengthofwall'])
        breadthofwall = float(request.POST['Breadthofwall'])
        thicknessofwall = float(request.POST['thicknessofwall'])
        lengthofbrick = float(request.POST["lengthofbrick"])
        breadthofbrick = float(request.POST["breadthofbrick"])
        thicknessofbrick = float(request.POST["thicknessofbrick"])
        units = request.POST["units"]
        brickunits = request.POST["brickunits"]
        
        volume_of_wall = lengthofwall * breadthofwall * thicknessofwall
        volume_of_brick = lengthofbrick * breadthofbrick * thicknessofbrick
        
        if units == 'mm':
            volume_of_wall = volume_of_wall/((304.8)**3)
        elif units == 'cm':  
            volume_of_wall = volume_of_wall/((30.48)**3)
        elif units == 'm':  
            volume_of_wall = volume_of_wall/((0.3048)**3)
        elif units == 'feet':  
            volume_of_wall = volume_of_wall/((1)**3)
           
            
        if brickunits == 'mm':
            volume_of_brick = volume_of_brick/((304.8)**3)
        elif brickunits == 'cm':  
            volume_of_brick = volume_of_brick/((30.48)**3 )
        elif brickunits == 'm':  
            volume_of_brick = volume_of_brick/((0.3048)**3)
        elif brickunits == 'feet':  
            volume_of_brick = volume_of_brick/((1)**3)    
            
            
        number_of_bricks = volume_of_wall/volume_of_brick
        wastage_of_bricks = (10/100)*number_of_bricks

        total_number_of_bricks =int  (number_of_bricks+wastage_of_bricks)


    context = {
        'volume_of_wall':volume_of_wall,
        'volume_of_brick':volume_of_brick,
        'total_number_of_bricks':total_number_of_bricks   
    }

    return render(request,'index.html',context)