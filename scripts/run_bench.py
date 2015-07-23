import argparse
import os

minmax  = 0
minsum  = 10
mincard = 10


GRINGO = './gringo '
CLASP  = './clasp '
UNCLASP= CLASP
HCLASP = CLASP

instance_dir = "./instances"

IREACTIONS = "encodings/ireactions.lp "
EXPANSION  = "encodings/card_min_completions_all_targets.lp "
MINMAX     = "encodings/minmax.lp "
MINSUM     = "encodings/sum.lp "
MINCARD    = "encodings/card.lp "
# HEURISTIC  = "encodings/heuristic.lp"


instances =  os.listdir(instance_dir)

for filename in instances:

  instance = os.path.join(instance_dir,filename)	

  # create ireactions
  command = GRINGO+instance+" "+IREACTIONS+"|"+CLASP+" --outf=1 | sed -e 's/ANSWER//g' > temp.lp"
  os.system(command)
  ireactions = "temp.lp "

  # solve problem 1
  command = GRINGO+instance+" "+ireactions+EXPANSION+MINCARD+"| "+CLASP+"0"
  print command
  os.system(command)

  # solve problem 2
  command = GRINGO+instance+" "+ireactions+EXPANSION+MINSUM+"| "+CLASP+"0"
  print command
  os.system(command)

  # solve problem 3
  command = GRINGO+instance+" "+ireactions+EXPANSION+MINMAX+MINCARD+"| "+CLASP+"0"
  print command
  os.system(command)

  # solve problem 4
  command = GRINGO+instance+" "+ireactions+EXPANSION+MINMAX+MINSUM+"| "+CLASP+"0"
  print command
  os.system(command)

  # solve problem 5
  command = GRINGO+instance+" "+ireactions+EXPANSION+MINCARD+MINMAX+"| "+CLASP+"0"
  print command
  os.system(command)

  # solve problem 6
  command = GRINGO+instance+" "+ireactions+EXPANSION+MINSUM+MINMAX+"| "+CLASP+"0"
  print command
  os.system(command)

  # solve problem 7
  command = GRINGO+instance+" "+ireactions+EXPANSION+MINSUM+MINCARD+"| "+CLASP+"0"
  print command
  os.system(command)

  # solve problem 8
  command = GRINGO+instance+" "+ireactions+EXPANSION+MINCARD+MINSUM+"| "+CLASP+"0"
  print command
  os.system(command)

  # solve problem 9
  command = GRINGO+instance+" "+ireactions+EXPANSION+MINMAX+MINSUM+MINCARD+"| "+CLASP+"0"
  print command
  os.system(command)

  # solve problem 10
  command = GRINGO+instance+" "+ireactions+EXPANSION+MINMAX+MINCARD+MINSUM+"| "+CLASP+"0"
  print command
  os.system(command)

  # solve problem 11
  command = GRINGO+instance+" "+ireactions+EXPANSION+MINSUM+MINMAX+MINCARD+"| "+CLASP+"0"
  print command
  os.system(command)

  # solve problem 12
  command = GRINGO+instance+" "+ireactions+EXPANSION+MINCARD+MINMAX+MINSUM+"| "+CLASP+"0"
  print command
  os.system(command)

  # solve problem 13
  command = GRINGO+instance+" "+ireactions+EXPANSION+MINCARD+MINSUM+MINMAX+"| "+CLASP+"0"
  print command
  os.system(command)

  # solve problem 14
  command = GRINGO+instance+" "+ireactions+EXPANSION+MINSUM+MINCARD+MINMAX+"| "+CLASP+"0"
  print command
  os.system(command)


# cleanup
# os.system("rm temp.lp")

# 
# 
# case $2 in
#     opt1)
#         $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO $EXPANSION $MINCARD $MINSUM $MINMAX | $CLASP
#         ;;
#     opt4)
#         $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO $EXPANSION $MINCARD $MINMAX | $CLASP
#         ;;
#     opt5)
#         $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO $EXPANSION $MINCARD $MINSUM | $CLASP
#         ;;
#     opt8)
#         $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO $EXPANSION $MINCARD | $CLASP
#         ;;
#     1)
#         if [ $# -ne 4 ] 
#         then
#             echo $"Usage: $0 INSTANCE_DIR 1 MINMAX MINSUM"
#             exit 1
#         fi
#         $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $HEURISTIC $MINSUM -c maxsum=$4 $MINMAX -c maxdist=$3 | $HCLASP -e record --opt-mode ignore 0
#         ;;
#     2)
#         if [ $# -ne 5 ] 
#         then
#             echo $"Usage: $0 INSTANCE_DIR 2 MINMAX MINSUM MINCARD"
#             exit 1
#         fi
#         $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $MINCARD -c maxcard=$5 $MINSUM -c maxsum=$4 $MINMAX -c maxdist=$3 | $CLASP --opt-mode ignore 0
#         ;;
#     3)
#         if [ $# -ne 3 ] 
#         then
#             echo $"Usage: $0 INSTANCE_DIR 3 MINMAX"
#             exit 1
#         fi
#         $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $HEURISTIC $MINMAX -c maxdist=$3 | $HCLASP -e record --opt-mode ignore 0
#         ;;
#     4)
#         if [ $# -ne 4 ] 
#         then
#             echo $"Usage: $0 INSTANCE_DIR 4 MINMAX MINCARD"
#             exit 1
#         fi
#         $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $MINCARD -c maxcard=$4 $MINMAX -c maxdist=$3 | $CLASP --opt-mode ignore 0
#         ;;
#     5)
#         if [ $# -ne 3 ] 
#         then
#             echo $"Usage: $0 INSTANCE_DIR 5 MINSUM"
#             exit 1
#         fi
#         $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $HEURISTIC $MINSUM -c maxsum=$3 | $HCLASP -e record --opt-mode ignore 0
#         ;;
#     6)
#         if [ $# -ne 4 ] 
#         then
#             echo $"Usage: $0 INSTANCE_DIR 6 MINSUM MINCARD"
#             exit 1
#         fi
#         $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $MINCARD -c maxcard=$4 $MINSUM -c maxsum=$3 | $CLASP --opt-mode ignore 0
#         ;;
#     7)
#         $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $HEURISTIC | $HCLASP -e record 0
#         ;;
#     8)
#         if [ $# -ne 3 ] 
#         then
#             echo $"Usage: $0 INSTANCE_DIR 8 MINCARD"
#             exit 1
#         fi
#         $GRINGO $IREACTIONS | $CLASP --outf=1 | sed -e 's/ANSWER//g' | $GRINGO - $EXPANSION $MINCARD -c maxcard=$3 | $CLASP --opt-mode ignore 0
#         ;;
#     *)
#         echo $"Usage: $0 INSTANCE_DIR [opt1|opt4|opt5|opt8|1|...|8]"
#         exit 1
# esac
