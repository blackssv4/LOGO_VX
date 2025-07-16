#!/bin/bash

# Tool path (current directory)
tool_dir="$(pwd)"

# Hide all files (except this script)
for item in "$tool_dir"/*; do
  filename=$(basename "$item")
  if [[ "$filename" != "$(basename "$0")" && "$filename" != .* ]]; then
    mv "$tool_dir/$filename" "$tool_dir/.${filename}"
  fi
done

# Color codes
RED='\033[1;31m'
GREEN='\033[1;32m'
YELLOW='\033[1;33m'
BLUE='\033[1;34m'
CYAN='\033[1;36m'
RESET='\033[0m'

# Display LOGO_VX banner
clear
echo -e "${RED}"
echo "██╗░░░░░░█████╗░░██████╗░░█████╗░██╗░░░██╗"
echo "██║░░░░░██╔══██╗██╔════╝░██╔══██╗╚██╗░██╔╝"
echo "██║░░░░░██║░░██║██║░░██╗░██║░░██║░╚████╔╝░"
echo "██║░░░░░██║░░██║██║░░╚██╗██║░░██║░░╚██╔╝░░"
echo "███████╗╚█████╔╝╚██████╔╝╚█████╔╝░░░██║░░░"
echo "╚══════╝░╚════╝░░╚═════╝░░╚════╝░░░░╚═╝░░░"
echo -e "${YELLOW}       🔥 By HA11 And BLACK 🔥  ${RESET}"
echo ""
echo -e "${CYAN}================================${RESET}"
echo -e "${GREEN}     Select a script to run      ${RESET}"
echo -e "${CYAN}================================${RESET}"
echo -e "${YELLOW}  [1]${RESET} For_Termux"
echo -e "${YELLOW}  [2]${RESET} For_Linux"
echo -e "${CYAN}==============================${RESET}"
read -p "$(echo -e $BLUE'Enter number: '$RESET)" choice

# Execute based on choice
case $choice in
  1)
    if [[ -f "$tool_dir/.For_Termux.py" ]]; then
      mv "$tool_dir/.3d.flf" "$tool_dir/3d.flf"
      mv "$tool_dir/.For_Termux.py" "$tool_dir/For_Termux.py"
      echo -e "${GREEN}✅ Running For_Termux...${RESET}"
      python3 "$tool_dir/For_Termux.py"
      mv "$tool_dir/For_Termux.py" "$tool_dir/.For_Termux.py"
      mv "$tool_dir/3d.flf" "$tool_dir/.3d.flf"
    else
      echo -e "${RED}❌ For_Termux.py not found${RESET}"
    fi
    ;;
  2)
    if [[ -f "$tool_dir/.For_Linux.py" ]]; then
      mv "$tool_dir/.starwars.flf" "$tool_dir/starwars.flf"
      mv "$tool_dir/.For_Linux.py" "$tool_dir/For_Linux.py"
      echo -e "${GREEN}✅ Running For_Linux...${RESET}"
      python3 "$tool_dir/For_Linux.py"
      mv "$tool_dir/starwars.flf" "$tool_dir/.starwars.flf"
      mv "$tool_dir/For_Linux.py" "$tool_dir/.For_Linux.py"
    else
      echo -e "${RED}❌ For_Linux.py not found${RESET}"
    fi
    ;;
  *)
    echo -e "${RED}❌ Invalid choice${RESET}"
    ;;
esac
