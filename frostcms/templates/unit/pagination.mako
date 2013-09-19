<div class="right_foot">
            	<div class="pagination">
                <ul>
          	 		% if items.first_page:
	          		<li><a href="?page=${items.first_page}" title="第一页">&laquo; 第一页</a></li>
	         		% endif
	         		 % if items.previous_page:
	          		<li><a href="?page=${items.previous_page}" title="上一页">&laquo; 上一页</a></li>
	          		% endif
	         		% for i in range(items.page - 3,items.page):
			  		% if items.page_count>0 and i>=items.first_page:
					<li><a href="?page=${i}" class="number" title="${i}">${i}</a></li>
					% endif
			  		% endfor
	          		<li><a href="#" class="number current" title="${items.page}">${items.page}</a></li> 
	          		% for i in range(items.page+1, items.page + 3):
			  			% if items.page_count>0 and i<=items.last_page:
						<li><a href="?page=${i}" class="number" title="${i}"> ${i} </a></li>
			  			% endif
			 		% endfor
			  		% if items.next_page:
			  		<li><a href="?page=${items.next_page}" title="下一页">下一页 &raquo;</a></li>
			  		% endif
			  		% if items.last_page:
	          		<li><a href="?page=${items.last_page}" title="最后一页">最后一页 &raquo;</a></li> 
	          		% endif
          		</ul>
            	</div>
            </div>
        </div> 