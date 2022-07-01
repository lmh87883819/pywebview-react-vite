import React from 'react';
import tw, { styled } from 'twin.macro';

export const Box = styled.div`
  ${tw`
    w-full 
    h-screen 
    bg-black 
    flex 
    justify-center
    items-center
    text-white
    text-2xl 
  `}
`;

const App = () => {
  return (
    <Box>
      <button onClick={() => window.pywebview.api.toogle_fullscreen()}>Toggle fullscreen</button>
      <button onClick={() => window.pywebview.api.open_file_dialog(window)}>Toggle fullscreen</button>
    </Box>
  );
};

export default App;
