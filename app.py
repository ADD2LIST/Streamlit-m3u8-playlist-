import streamlit as st
import requests

def extract_m3u8_links(playlist_url):
    response = requests.get(playlist_url)
    response_content = response.text

    # Extract m3u8 links from the response_content
    m3u8_links = []
    lines = response_content.split('\n')
    for line in lines:
        if line.startswith('#EXTINF'):
            next_line = lines[lines.index(line) + 1]
            if next_line.endswith('.m3u8'):
                m3u8_links.append(next_line)

    return m3u8_links

# Streamlit app
def main():
    st.title("m3u8 Link Extractor")

    # Input URL
    playlist_url = st.text_input("Enter m3u8 Playlist URL")

    # Extract m3u8 links on button click
    if st.button("Extract Links"):
        if playlist_url:
            m3u8_links = extract_m3u8_links(playlist_url)
            st.success(f"Found {len(m3u8_links)} m3u8 links:")
            for link in m3u8_links:
                st.write(link)
        else:
            st.warning("Please enter a valid m3u8 Playlist URL")

if __name__ == "__main__":
    main()
          
