FROM archlinux/archlinux:latest
ARG PHOENIX_USER_NAME

# アップデート
RUN pacman -Syu --noconfirm

# ユーザー作成
RUN useradd --create-home --gid wheel --shell /bin/bash $PHOENIX_USER_NAME

# 基本パッケージインストール
RUN pacman -S --noconfirm base-devel git
RUN echo "%wheel ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
# yayインストール
USER $PHOENIX_USER_NAME
WORKDIR /home/$PHOENIX_USER_NAME
RUN git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si --noconfirm && cd ../ && rm -r yay

# パッケージインストール
RUN sudo pacman -S --noconfirm neovim fish fzf neofetch tree

# 設定
COPY --chown=$PHOENIX_USER_NAME:wheel phoenix_files/.bashrc /home/$PHOENIX_USER_NAME/
COPY --chown=$PHOENIX_USER_NAME:wheel phoenix_files/.config/ /home/$PHOENIX_USER_NAME/.config/
