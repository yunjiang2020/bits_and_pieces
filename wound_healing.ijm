//Step 1:
//Download the confluency mask stacks from CellCyteX.

//Step 2:
//Open the mask stacks in ImageJ:

//  Go to Plugins > Macros > Startup Macros.
//  Open your script in the Macro window.
//  Ensure Area Fraction is selected by navigating to Analyze > Set Measurements > Area Fraction.

//Step 3:
//For each stack of confluency masks:

//  Use the Wand Tool to select the wound area.
//  Add the selected area to the ROI Manager.
//  Run the script.

//Note: Ensure that only one ROI is selected in the ROI Manager for the first stack before proceeding.




roiManager("Select", 0); // Select the first ROI,should be only 1 ROI in the manager
for (i = 1; i <= nSlices; i++) { //measure wound area
    setSlice(i);
    run("Measure");
}

// Invert ROI for the rest of the image
run("Make Inverse");

for (i = 1; i <= nSlices; i++) {  //measure cell area
    setSlice(i);    
    run("Measure");
}

Results = nResults(); // measurements in the Results table
areas = newArray(Results); 

// Collect measurements from the Results table
for (j = 0; j < Results; j++) {
    areas[j] = getResult("%Area", j);
}

W_0 = areas[0]; // wound confluency at time point 0
W_t = newArray(nSlices); // wound region
C_t = newArray(nSlices); // cell region

// Populate W_t and C_t arrays
for (j = 0; j < nSlices; j++) {
    W_t[j] = areas[j];
    C_t[j] = areas[j + nSlices]; 
}

// Calculate RWD(%)
for (j = 0; j < nSlices; j++) {
    print((W_t[j] - W_0) / (C_t[j] - W_0)*100);
}

//delete ROI and measurements from the current stack
//clear for the next stack
run("Clear Results");
roiManager("Delete");