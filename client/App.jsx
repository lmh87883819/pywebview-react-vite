import React, { useState } from 'react';
import tw, { styled } from 'twin.macro';
import { file } from './util/filePathPort';

export const Box = styled.div`
  ${tw`
    w-full 
    min-h-screen 
    bg-black 
    flex 
    justify-center
    items-center
    text-white
    text-2xl  
    flex-col
    gap-y-3
  `}
`;

const App = () => {
  const [image, setImage] = useState();

  const openFile = async () => {
    const results = await window.pywebview.api.save_content();
    if(results?.length > 0) {
      setImage(results[0]);
    }
  };

  return (
    <Box>
      <button onClick={() => window.pywebview.api.toogle_fullscreen()}>Toggle fullscreen</button>
      <button onClick={openFile}>Choose Image File</button>
      {
        image && (
        <img
          width={500}
          src={file(image)}
          alt="Beautiful thagewgaew"
        />
        )
      }
    </Box>
  );
};

export default App;
