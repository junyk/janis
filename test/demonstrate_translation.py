import argparse
import atexit

# Import library of already defined inouts, steps and outputs

from pipeline_definition.pipeline_translator import PipelineTranslator

#Extend the translation system with user defined
import examples.bio_informatics

def main( opts ):
    def atExit():
        print("BYE!!")
    atexit.register( atExit )

    #Get specified file to translate
    pdfile = opts.pdfile

    # pdfile = "pd_1.yml"

    pdTranslator = PipelineTranslator()
    pdTranslator.translate(pdfile, outfile="/Users/mohammadbhuyan/Temp/out.pdx", overwrite_outfile=True)
    #pdx.translate(pdfile, outfile="/Users/mohammadbhuyan/Temp/out.pdx")


if __name__ == "__main__":
    argprsr = argparse.ArgumentParser()
    argprsr.add_argument('pdfile', help='Pipeline Definition file.')
    opts = argprsr.parse_args()
    main( opts )

