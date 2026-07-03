sed -i '275,278c\
        {/* Admin Portal Nav option */}\
        <button\
          onClick={() => navigate(isAdminLoggedIn ? '"'"'/admin'"'"' : '"'"'/admin/login'"'"')}' src/views/ProfileView.tsx
