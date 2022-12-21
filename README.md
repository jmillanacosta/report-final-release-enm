# NanoSolveIT-D1.5
## Report on the final release of the eNanoMapper ontology

The updated eNanoMapper ontology release uses GitHub Actions for the build and QC.

The build of the slims is carried out in this repository through the actions contained in the .github/workflows folder, and the resulting slims of external ontologies are commited and pushed automatically to this repository when the build workflow is run. After that, robot diff and robot report are performed for quality control on the resulting ontology, with their results being stored under /report after each workflow run.

The configuration file enanomapper.yaml is used by the python setup scripts to update the YAML for these workflows (build, QC) on push via the update repository workflow.

![image](https://user-images.githubusercontent.com/83466805/208883091-69090194-e9b1-4c19-96c0-e20e5813d947.png)

### Some statistics about the usage of the ontology in the BioMax NanoSolveIT Knowledge Base:

<iframe src="sunburst1.html" style="position:sticky; left:0; 
width:100%; height:100%; border: none;"></iframe>

<iframe src="sunburst2.html" style="position:sticky; left:0; 
width:100%; height:100%; border: none;"></iframe>

<iframe src="sunburst3.html" style="position:sticky; left:0; 
width:100%; height:100%; border: none;"></iframe>

<iframe src="sunburst4.html" style="position:sticky; left:0; 
width:100%; height:100%; border: none;"></iframe>

  <div style="width:728px; height:728px; position:sticky; left:0;">
      <h2>Sankey flowchart </h2>
      <iframe src="sankey.html" style="position:sticky; left:0; 
          width:100%; height:100%; border: none;"></iframe>
          
Original data table: 

  <h2>Original data table</h2>
  <iframe src="table.html" style="position:sticky; left:0; 
        width:100%; height:100%; border: none;"></iframe>
