def drawboardGomoku(board):
   # create a 8" x 8" board
  fig = plt.figure(figsize=[9,7])
  fig.clear(True) 

  n = 15

#  fig.patch.set_facecolor((.8,.8,.8))

  ax = fig.add_subplot(111)

  for x in range(n):
    ax.plot([x+1, x+1], [0,n-1 ], 'k')
  for y in range(n):
    ax.plot([0, n-1], [y,y], 'k') 

# scale the axis area to fill the whole figure
  ax.set_position([0,0,1,1.1])

# get rid of axes and everything (the figure background will show through)
#  ax.set_axis_off()

# scale the plot area conveniently (the board is in 0,0..18,18)
  ax.set_xlim(-1,n)
#ax.set_ylim(-1,n)
  ty = ['1','2', '3', '4', '5', '6','7', '8', '9', '10', '11','12','13', '14', '15']
  tx = ['a', 'b', 'c', 'd', 'e','f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o']

  plt.xticks(range(len(tx)), tx)
  plt.yticks(range(len(ty)), ty)
  mov = 0
  for r in range(n):

     for j in range(n):

       x = board[n*r + j]
      
       if x > 0:
         s1, = ax.plot( r, j,'o',markersize=25, markeredgecolor=(0,0,0), markerfacecolor='k', markeredgewidth=2)
         s3 = ax.text( r,j,str(abs(x)-1),color = 'white', fontsize=10,horizontalalignment='center',verticalalignment='center')
       if x < 0:
         s1, = ax.plot(r,j,'o',markersize=25, markeredgecolor=(0,0,0), markerfacecolor='w', markeredgewidth=2)
         s3 = ax.text( r,j,str(abs(x)-1),color = 'black',fontsize=10,horizontalalignment='center',verticalalignment='center')
       i = x * 7 + r
       
  plt.show()