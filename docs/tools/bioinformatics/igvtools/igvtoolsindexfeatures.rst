:orphan:

IGVTools: Index Features
================================================

``IgvToolsIndexFeatures`` · *0 contributors · 1 version*

No documentation was provided: `contribute one <https://github.com/PMCC-BioinformaticsCore/janis-bioinformatics>`_


Quickstart
-----------

    .. code-block:: python

       from janis_bioinformatics.tools.igvtools.index.versions import IgvIndexFeature_2_5_3

       wf = WorkflowBuilder("myworkflow")

       wf.step(
           "igvtoolsindexfeatures_step",
           IgvIndexFeature_2_5_3(
               inp=None,
           )
       )
       wf.output("out", source=igvtoolsindexfeatures_step.out)
    

*OR*

1. `Install Janis </tutorials/tutorial0.html>`_

2. Ensure Janis is configured to work with Docker or Singularity.

3. Ensure all reference files are available:

.. note:: 

   More information about these inputs are available `below <#additional-configuration-inputs>`_.



4. Generate user input files for IgvToolsIndexFeatures:

.. code-block:: bash

   # user inputs
   janis inputs IgvToolsIndexFeatures > inputs.yaml



**inputs.yaml**

.. code-block:: yaml

       inp: inp.vcf




5. Run IgvToolsIndexFeatures with:

.. code-block:: bash

   janis run [...run options] \
       --inputs inputs.yaml \
       IgvToolsIndexFeatures





Information
------------

:ID: ``IgvToolsIndexFeatures``
:URL: *No URL to the documentation was provided*
:Versions: 2.5.3
:Container: quay.io/biocontainers/igvtools:2.5.3--0
:Authors: 
:Citations: None
:Created: None
:Updated: None


Outputs
-----------

======  ==========  ===============
name    type        documentation
======  ==========  ===============
out     IndexedVCF
======  ==========  ===============


Additional configuration (inputs)
---------------------------------

======  ======  ========  ==========  ===============
name    type    prefix      position  documentation
======  ======  ========  ==========  ===============
inp     VCF                        1
======  ======  ========  ==========  ===============

Workflow Description Language
------------------------------

.. code-block:: text

   version development

   task IgvToolsIndexFeatures {
     input {
       Int? runtime_cpu
       Int? runtime_memory
       Int? runtime_seconds
       Int? runtime_disks
       File inp
     }
     command <<<
       set -e
       cp -f ~{inp} sample.vcf
       igvtools index \
         sample.vcf
     >>>
     runtime {
       cpu: select_first([runtime_cpu, 1])
       disks: "local-disk ~{select_first([runtime_disks, 20])} SSD"
       docker: "quay.io/biocontainers/igvtools:2.5.3--0"
       duration: select_first([runtime_seconds, 86400])
       memory: "~{select_first([runtime_memory, 4])}G"
       preemptible: 2
     }
     output {
       File out = "sample.vcf"
       File out_idx = "sample.vcf" + ".idx"
     }
   }

Common Workflow Language
-------------------------

.. code-block:: text

   #!/usr/bin/env cwl-runner
   class: CommandLineTool
   cwlVersion: v1.0
   label: 'IGVTools: Index Features'

   requirements:
   - class: ShellCommandRequirement
   - class: InlineJavascriptRequirement
   - class: InitialWorkDirRequirement
     listing:
     - entryname: sample.vcf
       entry: $(inputs.inp)
   - class: DockerRequirement
     dockerPull: quay.io/biocontainers/igvtools:2.5.3--0

   inputs:
   - id: inp
     label: inp
     type: File
     inputBinding:
       position: 1

   outputs:
   - id: out
     label: out
     type: File
     secondaryFiles:
     - .idx
     outputBinding:
       glob: $(inputs.inp)
       loadContents: false
   stdout: _stdout
   stderr: _stderr

   baseCommand:
   - igvtools
   - index
   arguments: []
   id: IgvToolsIndexFeatures


