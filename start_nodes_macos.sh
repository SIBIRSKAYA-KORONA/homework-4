java \
  -Dwebdriver.chrome.driver="./chromedriver_macos" \
  -Dwebdriver.gecko.driver="./geckodriver_macos" \
  -jar selenium-server-standalone-3.141.59.jar \
  -role node -hub http://localhost:4444/grid/register \
  -browser browserName=chrome,maxInstances=2 \
  -browser browserName=firefox,maxInstances=2
