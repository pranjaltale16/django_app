<script>
        function check()
                {
                        p = document.getElementById('p1');
                        q = document.getElementById('p2');
                                if(p == q)
                                        window.location.assign({% url 'bookmarks:authenticate' %});
                                else
                                        alert("Password does not match");       
</script>

